"""For encapsulating the results of an event scan in a single instance."""

# fmt: off
# pylint: skip-file
# flake8: noqa

import itertools as it
import json
import logging
import pickle
from functools import cached_property
from pathlib import Path
from typing import Any, Dict, Final, List, Optional, Tuple, TypedDict, Union

import healpy  # type: ignore[import]
import matplotlib  # type: ignore[import]
import meander  # type: ignore[import]
import numpy as np
import pandas as pd  # type: ignore[import]
from astropy.io import ascii  # type: ignore[import]
from matplotlib import patheffects
from matplotlib import pyplot as plt
from matplotlib import text

from .event_metadata import EventMetadata
from .plot.plotting_tools import (
    DecFormatter,
    RaFormatter,
    format_fits_header,
    hp_ticklabels,
    plot_catalog,
)

###############################################################################
# CONSTANTS


# bookkeeping for comparing values
DEFAULT_RTOL_PER_FIELD = {  # w/ rtol values
    # any field not here is assumed to require '==' for comparison
    "llh": 1e-4,
    "E_in": 1e-2,
    "E_tot": 1e-2,
}
ZERO_MAKES_FIELD_ALWAYS_ISCLOSE = [
    # if a pixel field's val is 0, then that datapoint is "isclose" to any value
    "E_in",
    "E_tot",
]


###############################################################################
# DATA TYPES


class PyDictNSidePixels(TypedDict):
    columns: List[str]
    metadata: Dict[str, Any]
    data: List[List[Union[int, float]]]


PyDictResult = Dict[str, PyDictNSidePixels]


###############################################################################
# MAIN CLASS

class SkyScanResult:
    """This class parses a scan result and stores the relevant numeric results
    of the scan. Ideally it should serve as the basic data structure for
    plotting / processing / transmission of the scan result.

    `result` is a dictionary keyed by 'nside: str' values for which a scan
    result is available (e.g. 8, 64, 512).

    The scan result is a dictionary:
    - i (pixel index, integer) ->
        'frame', 'llh', 'recoLossesInside', 'recoLossesTotal'

    The numeric values of interest are 'llh', 'recoLossesInside',
    'recoLossesTotal'. The pixel indices in the input dictionary are in
    general unsorted (python dict are unsorted by design) and are
    incomplete (since fine-grained scans only cover a portion of the
    HEALPIX area). The class stores the each result in a np
    structured array sorted by the pixel index, which is stored in a
    dedicated field.

    TODO: implement FITS output.
    """

    PIXEL_TYPE = np.dtype(
        [("index", int), ("llh", float), ("E_in", float), ("E_tot", float)]
    )
    PIXEL_FIELDS: Tuple[str, ...] = PIXEL_TYPE.names  # type: ignore[assignment]
    ATOL = 1.0e-8  # 1.0e-8 is the default used by np.isclose()

    MINIMAL_METADATA_FIELDS: Final[List[str]] = "run_id event_id mjd event_type nside".split()

    def __init__(self, result: Dict[str, np.ndarray]):
        self.logger = logging.getLogger(__name__)

        # validate result data
        if not isinstance(result, dict):
            raise ValueError("'result' must be an instance of Dict[str, np.ndarray]")
        for nside in result:
            try:
                self.parse_nside(nside)
            except (KeyError, ValueError) as e:
                raise ValueError(f"'result' has invalid nside key: {nside}") from e
            if not isinstance(result[nside], np.ndarray):
                raise ValueError("'result' must be an instance of Dict[str, np.ndarray]")
            if result[nside].dtype != self.PIXEL_TYPE:
                raise ValueError(
                    f"'result' has invalid dtype {result[nside].dtype} "
                    f"should be {self.PIXEL_TYPE}"
                )
        self.result = result
        self.nsides = sorted([self.parse_nside(key) for key in self.result])

        self.logger.debug(f"Metadata for this result: {[self.result[_].dtype.metadata for _ in self.result]}")



    """
    Comparison operators and methods
    """

    def __eq__(self, other: object) -> bool:
        """Are the two instance's result lists strictly equal?"""
        if not isinstance(other, SkyScanResult):
            return False
        if self.result.keys() != other.result.keys():
            return False
        # NOTE: will return false if NaN are present
        # np.array_equal() supports `equal_nan` option only from version 1.19
        return all(
            np.array_equal(self.result[nside], other.result[nside])
            for nside in self.result
        )

    def isclose_datapoint(
        self,
        s_val: float,
        o_val: float,
        field: str,
        equal_nan: bool,
        rtol_per_field: Dict[str, float],
    ) -> Tuple[float, bool]:
        """Get the diff float-value and test truth-value for the 2 pixel
        datapoints."""
        if field not in rtol_per_field:
            raise ValueError(
                f"Datapoint field ({field}) cannot be compared by "
                f"'is_close_datapoint()', must use '=='"
            )
        if field in ZERO_MAKES_FIELD_ALWAYS_ISCLOSE and (s_val == 0.0 or o_val == 0.0):
            return float("nan"), True
        try:
            rdiff = (abs(s_val - o_val) - self.ATOL) / abs(o_val)  # used by np.isclose
        except ZeroDivisionError:
            rdiff = float("inf")
        return (
            rdiff,
            bool(
                np.isclose(
                    s_val,
                    o_val,
                    equal_nan=equal_nan,
                    rtol=rtol_per_field[field],
                    atol=self.ATOL,
                )
            ),
        )

    def isclose_pixel(
        self,
        sre_pix: np.ndarray,
        ore_pix: np.ndarray,
        equal_nan: bool,
        rtol_per_field: Dict[str, float],
    ) -> Tuple[List[float], List[bool]]:
        """Get the diff float-values and test truth-values for the 2 pixel-
        data.

        The datapoints are compared face-to-face (zipped).
        """
        diff_vals = []
        test_vals = []

        for s_val, o_val, field in zip(sre_pix, ore_pix, self.PIXEL_FIELDS):
            s_val, o_val = float(s_val), float(o_val)

            # CASE: a "require close" datapoint
            if field in rtol_per_field:
                diff, test = self.isclose_datapoint(s_val, o_val, field, equal_nan, rtol_per_field)
            # CASE: a "require equal" datapoint
            else:
                diff, test = s_val - o_val, s_val == o_val

            diff_vals.append(diff)
            test_vals.append(test)

        return diff_vals, test_vals

    def has_minimal_metadata(self) -> bool:
        """Check that the minimum metadata is set."""
        for mk in self.MINIMAL_METADATA_FIELDS:
            for k in self.result:
                if self.result[k].dtype.metadata is None:
                    return False
                if mk not in self.result[k].dtype.metadata:
                    return False
        return True

    def get_event_metadata(self) -> EventMetadata:
        """Get the EventMetadata portion of the result's metadata."""
        if self.has_minimal_metadata():
            first_metadata = self.result[list(self.result.keys())[0]].dtype.metadata
            return EventMetadata(
                first_metadata['run_id'],
                first_metadata['event_id'],
                first_metadata['event_type'],
                first_metadata['mjd'],
                first_metadata.get('is_real_event', False),  # assume simulated event
            )
        else:
            self.logger.warning("Metadata doesn't seem to exist and will not be used for plotting.")
            return EventMetadata(0, 0, '', 0, False)

    def isclose_nside(self,
        other: "SkyScanResult",
        equal_nan: bool,
        rtol_per_field: Dict[str, float],
        nside: str,
    ) -> Tuple[bool, List[Tuple[Tuple[Any, ...], Tuple[Any, ...], Tuple[float, ...], Tuple[bool, ...]]]]:
        """Get whether the two nside's pixels are all "close"."""
        # zip-iterate each pixel-data
        nside_diffs = []
        for sre_pix, ore_pix in it.zip_longest(
            self.result.get(nside, []),  # empty-list -> fillvalue
            other.result.get(nside, []),  # empty-list -> fillvalue
            fillvalue=np.full((len(self.PIXEL_FIELDS),), np.nan),  # 1 vector
        ):
            diff_vals, test_vals = self.isclose_pixel(
                sre_pix, ore_pix, equal_nan, rtol_per_field
            )
            pix_diff = (
                tuple(sre_pix.tolist()),
                tuple(ore_pix.tolist()),
                tuple(diff_vals),  # diff float-value
                tuple(test_vals),  # test truth-value
            )
            for vals in pix_diff:
                self.logger.debug(f"{nside}: {vals}")
            nside_diffs.append(pix_diff)

        # aggregate test-truth values
        nside_equal = {
            field: all(d[3][self.PIXEL_FIELDS.index(field)] for d in nside_diffs)
            for field in set(self.PIXEL_FIELDS) - set(rtol_per_field)
        }
        nside_close = {
            field: all(d[3][self.PIXEL_FIELDS.index(field)] for d in nside_diffs)
            for field in rtol_per_field
        }

        # log results (test-truth values)
        if not all(nside_equal.values()):
            self.logger.info(f"Mismatched pixel indices for nside={nside}")
        if not all(nside_close.values()):
            self.logger.info(f"Mismatched numerical results for nside={nside}")
            self.logger.debug(f"{nside_close}")

        return all(nside_equal.values()) and all(nside_close.values()), nside_diffs

    def is_close(
        self,
        other: "SkyScanResult",
        equal_nan: bool = True,
        dump_json_diff: Optional[Path] = None,
        rtol_per_field: Optional[Dict[str, float]] = None,
    ) -> bool:
        """Checks if two results are close by requiring strict equality on
        pixel indices and close condition on numeric results.

        Args:
            `other`
                the instance to compare
            `equal_nan`
                whether to let `nan == nan` be True
                (default: `True`)
            `dump_json_diff`
                get a json file containing every comparison at the pixel-data level
                (default: `None`)
            `rtol_per_field`
                a mapping of each field to a rtol value
                (default: `DEFAULT_RTOL_PER_FIELD`)

        Returns:
            bool: True if `other` and `self` are close
        """
        if not rtol_per_field:
            rtol_per_field = DEFAULT_RTOL_PER_FIELD

        close: Dict[str, bool] = {}  # one bool for each nside value
        diffs: Dict[str, list] = {}  # (~4x size of self.results) w/ per-pixel info

        # now check individual nside-iterations
        for nside in sorted(self.result.keys() & other.result.keys(), reverse=True):
            self.logger.info(f"Comparing for nside={nside}")
            # Q: why aren't we using np.array_equal and np.allclose?
            # A: we want detailed pixel-level diffs w/out repeating detailed code
            close[nside], diffs[nside] = self.isclose_nside(
                other, equal_nan, rtol_per_field, nside
            )

        # finish up
        self.logger.info(f"Comparison result: {close}")

        if dump_json_diff:
            with open(dump_json_diff, "w") as f:
                self.logger.info(f"Writing diff to {dump_json_diff}...")
                json.dump(diffs, f, indent=3)

        return all(close.values())

    """
    Auxiliary methods
    """

    @staticmethod
    def format_nside(nside) -> str:
        return f"nside-{nside}"

    @staticmethod
    def parse_nside(key) -> int:
        return int(key.split("nside-")[1])

    def get_nside_string(self) -> str:
        """Returns a string string listing the nside values to be included in
        the output filename."""
        # keys have a 'nside-NNN' format but we just want to extract the nside values to build the string
        # parsing back and forth numbers to strings is not the most elegant choice but works for now
        # TODO: possibly better to use integer values as keys in self.result
        return "_".join([str(nside) for nside in self.nsides])

    def get_filename(
        self,
        event_metadata: EventMetadata,
        extension: str,
        output_dir: Union[str, Path, None] = None
    ) -> Path:
        """Make a filepath for writing representations of `self` to disk."""
        if not extension.startswith('.'):
            extension = '.' + extension

        if nside_string := self.get_nside_string():
            filename = Path(f"{str(event_metadata)}_{nside_string}{extension}")
        else:
            raise ValueError("cannot create filename for an empty result")

        if output_dir is not None:
            filename = output_dir / Path(filename)
        return filename

    """
    NPZ input / output
    """

    @classmethod
    def read_npz(cls, filename: Union[str, Path]) -> "SkyScanResult":
        """Load from .npz file."""
        npz = np.load(filename)
        result = dict()
        if "header" not in npz:
            for key in npz.keys():
                result[key] = npz[key]
        else:
            h = npz["header"]
            for v in h:
                key = cls.format_nside(v['nside'])
                _dtype = np.dtype(
                    npz[key].dtype,
                    metadata={k:value for k, value in zip(h.dtype.fields.keys(), v)},  # type: ignore[call-overload]
                )
                result[key] = np.array(list(npz[key]), dtype=_dtype)
        return cls(result=result)

    def to_npz(
        self,
        event_metadata: EventMetadata,
        output_dir: Union[str, Path, None] = None,
    ) -> Path:
        """Save to .npz file."""
        filename = self.get_filename(event_metadata, '.npz', output_dir)

        try:
            first = next(iter(self.result.values()))
        except StopIteration: # no results yet
            np.savez(filename, **self.result)
            return Path(filename)

        try:
            metadata_dtype = np.dtype(
                [
                    (k, type(v)) if not isinstance(v, str) else (k, f"U{len(v)}")
                    for k, v in first.dtype.metadata.items()
                ],
            )
            header = np.array(
                [
                    tuple(self.result[k].dtype.metadata[mk] for mk in metadata_dtype.fields)  # type: ignore[union-attr]
                    for k in self.result
                ],
                dtype=metadata_dtype,
            )
            np.savez(filename, header=header, **self.result)
        except (TypeError, AttributeError):
            np.savez(filename, **self.result)

        return Path(filename)

    """
    JSON input / output
    """

    @classmethod
    def read_json(cls, filename: Union[str, Path]) -> "SkyScanResult":
        """Load from .json file."""
        with open(filename) as f:
            pydict = json.load(f)
        return cls.deserialize(pydict)

    def to_json(
        self,
        event_metadata: EventMetadata,
        output_dir: Union[str, Path, None] = None
    ) -> Path:
        """Save to .json file."""
        filename = self.get_filename(event_metadata, '.json', output_dir)
        pydict = self.serialize()
        with open(filename, 'w') as f:
            json.dump(pydict, f, indent=4)
        return filename

    """
    Serialize/deserialize (input / output)
    """

    @classmethod
    def deserialize(cls, pydict: PyDictResult) -> "SkyScanResult":
        """Deserialize from a python-native dict."""
        result = dict()

        for nside, pydict_nside_pixels in pydict.items():
            # validate keys
            if set(pydict_nside_pixels.keys()) != {'columns', 'metadata', 'data'}:
                raise ValueError(f"PyDictResult entry has extra/missing keys: {pydict_nside_pixels.keys()}")

            # check 'columns'
            if pydict_nside_pixels['columns'] != list(cls.PIXEL_FIELDS):
                raise ValueError(
                    f"PyDictResult entry has invalid 'columns' entry "
                    f"({pydict_nside_pixels['columns']}) should be {list(cls.PIXEL_FIELDS)}"
                )

            # check 'metadata'
            try:
                if pydict_nside_pixels['metadata']['nside'] != cls.parse_nside(nside):
                    raise ValueError(
                        f"PyDictResult entry has incorrect 'metadata'.'nside' value: "
                        f"{pydict_nside_pixels['metadata']['nside']} should be {cls.parse_nside(nside)}"
                    )
            except (KeyError, TypeError) as e:
                raise ValueError("PyDictResult entry has missing key 'nside'") from e

            # read/convert
            _dtype = np.dtype(
                cls.PIXEL_TYPE,
                metadata=pydict_nside_pixels['metadata'],  # type: ignore[call-overload]
            )
            result_nside_pixels = np.zeros(len(pydict_nside_pixels['data']), dtype=_dtype)
            for i, pix_4list in enumerate(sorted(pydict_nside_pixels['data'], key=lambda x: x[0])):
                result_nside_pixels[i] = tuple(pix_4list)

            result[nside] = result_nside_pixels

        return cls(result)

    def serialize(self) -> PyDictResult:
        """Serialize as a python-native dict.

        Example:
        {
            'nside-8': {
                "columns": [
                    "index",
                    "llh",
                    "E_in",
                    "E_tot"
                ],
                "metadata": {
                    "nside": 8,
                    ...
                }
                "data": [
                    [
                        0,
                        496.81227052,
                        4643.8910975498,
                        4736.3116335241
                    ],
                    [
                        1,
                        503.6851841852,
                        5058.9879730721,
                        585792.3192455448
                    ],
                    ...
                ]
            },
            ...
        }
        """
        pydict: PyDictResult = {}
        for nside in self.result:
            nside_data: np.ndarray = self.result[nside]
            df = pd.DataFrame(
                nside_data,
                columns=list(nside_data.dtype.names),
            )
            pydict[nside] = {k:v for k,v in df.to_dict(orient='split').items() if k != 'index'}  # type: ignore[assignment]
            pydict[nside]['metadata'] = dict()

            for key in nside_data.dtype.metadata:
                # dtype.metadata is a mappingproxy (dict-like) containing numpy-typed values
                # convert numpy types to python bultins to be JSON-friendly
                val = nside_data.dtype.metadata[key]
                if isinstance(val, np.generic):
                    # numpy type, non serializable
                    # convert to python built-in by calling item()
                    pydict[nside]['metadata'][key] = nside_data.dtype.metadata[key].item()
                else:
                    # likely a natively serializable python built-in 
                    pydict[nside]['metadata'][key] = val
        return pydict

    """
    Querying
    """

    def llh(self, ra, dec):
        for nside in self.nsides[::-1]:
            grid_pix = healpy.ang2pix(nside, np.pi/2 - dec, ra)
            _res = self.result[self.format_nside(nside)]
            llh = _res[_res['index']==grid_pix]['llh']
            if llh.size > 0:
                return llh

    @property
    def min_llh(self):
        return self.best_fit['llh']

    @cached_property
    def best_fit(self):
        _minllh = np.inf
        for k in self.result:
            _res = self.result[k]
            _min = _res['llh'].min()
            if _min < _minllh:
                _minllh = _min
                _bestfit = _res[_res['llh'].argmin()]
        return _bestfit

    @property
    def best_dir(self):
        minCoDec, minRA = healpy.pix2ang(self.best_fit.dtype.metadata['nside'], self.best_fit['index'])
        minDec = np.pi/2 - minCoDec
        return minRA, minDec

    """
    Plotting routines
    """

    plot_y_size_in = 3.85
    plot_x_size_in = 6
    plot_dpi_standard = 150
    plot_dpi_zoomed = 1200
    plot_colormap = matplotlib.colormaps['plasma_r']

    def check_result(self):
        """Check in legacy plotting code.
        """
        for k in self.result:
            if "nside-" not in k:
                raise RuntimeError("\"nside\" not in result file..")
    
    @staticmethod
    # Calculates are using Gauss-Green theorem / shoelace formula
    # TODO: vectorize using numpy.
    # Note: in some cases the argument is not a np.ndarray so one has to convert the data series beforehand.
    def calculate_area(vs) -> float:
        a = 0
        x0, y0 = vs[0]
        for [x1,y1] in vs[1:]:
            dx = x1-x0
            dy = y1-y0
            a += 0.5*(y0*dx - x0*dy)
            x0 = x1
            y0 = y1
        return a

    def create_plot(self, dozoom = False):

        dpi = self.plot_dpi_standard if not dozoom else self.plot_dpi_zoomed
        xsize = self.plot_x_size_in * dpi
        ysize = xsize // 2

        self.check_result()

        event_metadata = self.get_event_metadata()
        unique_id = f'{str(event_metadata)}_{self.get_nside_string()}'
        plot_title = f"Run: {event_metadata.run_id} Event {event_metadata.event_id}: Type: {event_metadata.event_type} MJD: {event_metadata.mjd}"

        plot_filename = f"{unique_id}.{'plot_zoomed_legacy.' if dozoom else ''}pdf"
        print(f"saving plot to {plot_filename}")

        nsides = self.nsides
        print(f"available nsides: {nsides}")

        min_value = np.nan
        max_value = np.nan
        minRA=0.
        minDec=0.

        # theta = np.linspace(np.pi, 0., ysize)
        dec = np.linspace(-np.pi/2., np.pi/2., ysize)

        # phi   = np.linspace(0., 2.*np.pi, xsize)
        ra = np.linspace(0., 2.*np.pi, xsize)

        # project the map to a rectangular matrix xsize x ysize
        RA, DEC = np.meshgrid(ra, dec)

        grid_map = None

        grid_pix = None

        # now plot maps above each other
        for nside in nsides:
            print(("constructing map for nside {0}...".format(nside)))
            # grid_pix = healpy.ang2pix(nside, THETA, PHI)
            grid_pix = healpy.ang2pix(nside, np.pi/2. - DEC, RA)
            this_map = np.ones(healpy.nside2npix(nside))*np.inf

            for pixel_data in self.result[f'nside-{nside}']:
                pixel = pixel_data['index']
                # show 2*delta_LLH
                value = 2*pixel_data['llh']
                if np.isfinite(value):
                    if np.isnan(min_value) or value < min_value:
                        minCoDec, minRA = healpy.pix2ang(nside, pixel)
                        minDec = np.pi/2 - minCoDec
                        min_value = value
                    if np.isnan(max_value) or value > max_value:
                        max_value = value
                this_map[pixel] = value

            if grid_map is None:
                grid_map = this_map[grid_pix]
            else:
                grid_map = np.where( np.isfinite(this_map[grid_pix]), this_map[grid_pix], grid_map)

            del this_map

            print(("done with map for nside {0}...".format(nside)))

        # clean up
        if grid_pix is not None:
            del grid_pix

        if grid_map is None:
            # create an "empty" map if there are no pixels at all
            grid_pix = healpy.ang2pix(8, np.pi/2 - DEC, RA)
            this_map = np.ones(healpy.nside2npix(8))*np.inf
            grid_map = this_map[grid_pix]
            del this_map
            del grid_pix

        print("min  RA:", minRA *180./np.pi, "deg,", minRA*12./np.pi, "hours")
        print("min dec:", minDec*180./np.pi, "deg")

        # renormalize
        if dozoom:
            grid_map = grid_map - min_value
            # max_value = max_value - min_value
            min_value = 0.
            max_value = 50

        grid_map = np.ma.masked_invalid(grid_map)

        print(f"preparing plot: {plot_filename}...")

        # the color map to use
        cmap = self.plot_colormap
        cmap.set_under(alpha=0.) # make underflows transparent
        cmap.set_bad(alpha=1., color=(1.,0.,0.)) # make NaNs bright red

        # prepare the figure canvas
        fig = matplotlib.pyplot.figure(figsize=(self.plot_x_size_in,self.plot_y_size_in))
        if dozoom:
            ax = fig.add_subplot(111) #,projection='cartesian')
        else:
            cmap.set_over(alpha=0.)  # make underflows transparent
            ax = fig.add_subplot(111,projection='astro mollweide')

        # rasterized makes the map bitmap while the labels remain vectorial
        # flip longitude to the astro convention
        image = ax.pcolormesh(ra, dec, grid_map, vmin=min_value, vmax=max_value, rasterized=True, cmap=cmap)
        # ax.set_xlim(np.pi, -np.pi)



        contour_levels = (np.array([1.39, 4.61, 11.83, 28.74])+min_value)[:2]
        contour_labels = [r'50%', r'90%', r'3$\sigma$', r'5$\sigma$'][:2]
        contour_colors=['k', 'r', 'g', 'b'][:2]
        leg_element=[]
        cs_collections = []
        for level, color in zip(contour_levels, contour_colors):
            CS = ax.contour(ra, dec, grid_map, levels=[level], colors=[color])
            cs_collections.append(CS.collections[0])
            e, _ = CS.legend_elements()
            leg_element.append(e[0])

        if not dozoom:
            # graticule
            # mypy error: "Axes" has no attribute "set_longitude_grid"  [attr-defined]
            ax.set_longitude_grid(30)
            # mypy error: "Axes" has no attribute "set_latitude_grid"  [attr-defined]
            ax.set_latitude_grid(30)
            cb = fig.colorbar(image, orientation='horizontal', shrink=.6, pad=0.05, ticks=[min_value, max_value])
            cb.ax.xaxis.set_label_text(r"$-2 \ln(L)$")
        else:
            ax.set_xlabel('right ascension')
            ax.set_ylabel('declination')
            cb = fig.colorbar(image, orientation='horizontal', shrink=.6, pad=0.13)
            cb.ax.xaxis.set_label_text(r"$-2 \Delta \ln (L)$")

            leg_labels = []
            for i in range(len(contour_labels)):
                vs = cs_collections[i].get_paths()[0].vertices
                # Compute area enclosed by vertices.
                # Take absolute values to be independent of orientation of the boundary integral.
                a = abs(self.calculate_area(vs)) # will be in square-radians
                a = a*(180.*180.)/(np.pi*np.pi) # convert to square-degrees

                leg_labels.append(f'{contour_labels[i]} - area: {a:.2f}sqdeg')

            ax.scatter(minRA, minDec, s=20, marker='*', color='black', label=r'scan best-fit', zorder=2)
            ax.legend(leg_element, leg_labels, loc='lower right', fontsize=8, scatterpoints=1, ncol=2)

            print("Contour Area (90%):", a, "degrees (cartesian)", a*np.cos(minDec)**2, "degrees (scaled)")
            x_width = 1.6 * np.sqrt(a)

            if np.isnan(x_width):
                # error: "QuadContourSet" has no attribute "allsegs"  [attr-defined]
                x_width = 1.6*(max(CS.allsegs[i][0][:,0]) - min(CS.allsegs[i][0][:,0]))
            print(x_width)
            y_width = 0.5 * x_width

            lower_x = max(minRA  - x_width*np.pi/180., 0.)
            upper_x = min(minRA  + x_width*np.pi/180., 2 * np.pi)
            lower_y = max(minDec -y_width*np.pi/180., -np.pi/2.)
            upper_y = min(minDec + y_width*np.pi/180., np.pi/2.)

            ax.set_xlim(upper_x, lower_x)
            ax.set_ylim(lower_y, upper_y)

            ax.xaxis.set_major_formatter(DecFormatter())
            ax.yaxis.set_major_formatter(DecFormatter())

            factor = 0.25*(np.pi/180.)
            while (upper_x - lower_x)/factor > 6:
                 factor *= 2.
            tick_label_grid = factor

            ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=tick_label_grid))
            ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=tick_label_grid))

        # cb.ax.xaxis.labelpad = -8
        # workaround for issue with viewers, see colorbar docstring
        # mypy compliance: since cb.solids could be None, we check that it is actually
        #   a valid object before accessing it
        if isinstance(cb.solids, matplotlib.collections.QuadMesh):
            cb.solids.set_edgecolor("face")

        if dozoom:
            ax.set_aspect('equal')
        ax.tick_params(axis='x', labelsize=10)
        ax.tick_params(axis='y', labelsize=10)

        # show the grid
        ax.grid(True, color='k', alpha=0.5)

        # Otherwise, add the path effects.
        effects = [patheffects.withStroke(linewidth=1.1, foreground='w')]
        # mypy warnings
        for artist in ax.findobj(text.Text):
            # mypy error: Argument 1 to "set_path_effects" of "Artist" has incompatible type "list[withStroke]"; expected "list[AbstractPathEffect]"  [arg-type]
            artist.set_path_effects(effects)

        # remove white space around figure
        spacing = 0.01
        if not dozoom:
            fig.subplots_adjust(bottom=spacing, top=1.-spacing, left=spacing+0.04, right=1.-spacing)
        else:
            fig.subplots_adjust(bottom=spacing, top=0.92-spacing, left=spacing+0.1, right=1.-spacing)

        # set the title
        fig.suptitle(plot_title)

        print(f"saving: {plot_filename}...")

        fig.savefig(plot_filename, dpi=dpi, transparent=True)

        print("done.")

    def create_plot_zoomed(self,
                           extra_ra=np.nan,
                           extra_dec=np.nan,
                           extra_radius=np.nan,
                           systematics=False,
                           plot_bounding_box=False,
                           plot_4fgl=False):
        """Uses healpy to plot a map."""

        def bounding_box(ra, dec, theta, phi):
            shift = ra-180

            ra_plus = np.max((np.degrees(phi)-shift)%360) - 180
            ra_minus = np.min((np.degrees(phi)-shift)%360) - 180
            dec_plus = (np.pi/2-np.min(theta))*180./np.pi - dec
            dec_minus = (np.pi/2-np.max(theta))*180./np.pi - dec
            return ra_plus, ra_minus, dec_plus, dec_minus

        dpi = self.plot_dpi_zoomed

        lonra=[-10.,10.]
        latra=[-10.,10.]

        self.check_result()

        event_metadata = self.get_event_metadata()
        unique_id = f'{str(event_metadata)}_{self.get_nside_string()}'
        plot_title = f"Run: {event_metadata.run_id} Event {event_metadata.event_id}: Type: {event_metadata.event_type} MJD: {event_metadata.mjd}"

        nsides = self.nsides
        print(f"available nsides: {nsides}")

        if systematics is not True:
            plot_filename = unique_id + ".plot_zoomed_wilks.pdf"
        else:
            plot_filename = unique_id + ".plot_zoomed.pdf"
        print("saving plot to {0}".format(plot_filename))

        nsides = self.nsides
        print(f"available nsides: {nsides}")

        grid_map = dict()
        max_nside = max(nsides)
        equatorial_map = np.full(healpy.nside2npix(max_nside), np.nan)

        for nside in nsides:
            print("constructing map for nside {0}...".format(nside))
            npix = healpy.nside2npix(nside)

            map_data = self.result[f'nside-{nside}']
            pixels = map_data['index']
            values = map_data['llh']
            this_map = np.full(npix, np.nan)
            this_map[pixels] = values
            if nside < max_nside:
                this_map = healpy.ud_grade(this_map, max_nside)
            mask = np.logical_and(~np.isnan(this_map), np.isfinite(this_map))
            equatorial_map[mask] = this_map[mask]

            for pixel_data in self.result[f"nside-{nside}"]:
                pixel = pixel_data['index']
                value = pixel_data['llh']
                if np.isfinite(value) and not np.isnan(value):
                    tmp_theta, tmp_phi = healpy.pix2ang(nside, pixel)
                    tmp_dec = np.pi/2 - tmp_theta
                    tmp_ra = tmp_phi
                    grid_map[(tmp_dec, tmp_ra)] = value
            print("done with map for nside {0}...".format(nside))

        grid_dec_list, grid_ra_list, grid_value_list = [], [], []

        for (dec, ra), value in grid_map.items():
            grid_dec_list.append(dec); grid_ra_list.append(ra)
            grid_value_list.append(value)
        grid_dec: np.ndarray = np.asarray(grid_dec_list)
        grid_ra: np.ndarray = np.asarray(grid_ra_list)
        grid_value: np.ndarray = np.asarray(grid_value_list)

        sorting_indices = np.argsort(grid_value)
        grid_value = grid_value[sorting_indices]
        grid_dec = grid_dec[sorting_indices]
        grid_ra = grid_ra[sorting_indices]

        min_value = grid_value[0]
        minDec = grid_dec[0]
        minRA = grid_ra[0]

        print("min  RA:", minRA *180./np.pi, "deg,", minRA*12./np.pi, "hours")
        print("min dec:", minDec*180./np.pi, "deg")

        # renormalize
        grid_value = grid_value - min_value
        min_value = 0.

        # show 2 * delta_LLH
        grid_value = grid_value * 2.

        # Do same for the healpy map
        equatorial_map[np.isinf(equatorial_map)] = np.nan
        equatorial_map -= np.nanmin(equatorial_map)
        equatorial_map *= 2.

        print("preparing plot: {0}...".format(plot_filename))

        cmap = self.plot_colormap
        cmap.set_under('w')
        cmap.set_bad(alpha=1., color=(1.,0.,0.)) # make NaNs bright red

        # Calculate the contours
        if systematics:
            # from Pan-Starrs event 127852
            contour_levels = (np.array([22.2, 64.2])+min_value) # these are values determined from MC by Will on the TS (2*LLH)
            contour_labels = [r'50% (IC160427A syst.)', r'90% (IC160427A syst.)']
            contour_colors=['k', 'r']
        else:
            # Wilks
            contour_levels = (np.array([1.39, 4.61, 11.83, 28.74])+min_value)[:3]
            contour_labels = [r'50%', r'90%', r'3$\sigma$', r'5$\sigma$'][:3]
            contour_colors=['k', 'r', 'g', 'b'][:3]

        sample_points = np.array([np.pi/2 - grid_dec, grid_ra]).T
        # Call meander module to find contours
        contours_by_level = meander.spherical_contours(sample_points,
            grid_value, contour_levels
            )
        # Check for RA values that are out of bounds
        for level in contours_by_level:
            for contour in level:
                contour.T[1] = np.where(contour.T[1] < 0.,
                    contour.T[1] + 2.*np.pi, contour.T[1]
                    )


        # Find the rough extent of the contours to bound the plot
        contours = contours_by_level[-1]
        ra = minRA * 180./np.pi
        dec = minDec * 180./np.pi
        theta, phi = np.concatenate(contours_by_level[-1]).T
        ra_plus, ra_minus, dec_plus, dec_minus = bounding_box(ra, dec, theta, phi)
        ra_bound = min(15, max(3, max(-ra_minus, ra_plus)))
        dec_bound = min(15, max(2, max(-dec_minus, dec_plus)))
        lonra = [-ra_bound, ra_bound]
        latra = [-dec_bound, dec_bound]

        #Begin the figure
        plt.clf()
        # Rotate into healpy coordinates
        lon, lat = np.degrees(minRA), np.degrees(minDec)
        healpy.cartview(map=equatorial_map, title=plot_title,
            min=0., #min 2DeltaLLH value for colorscale
            max=40., #max 2DeltaLLH value for colorscale
            rot=(lon,lat,0.), cmap=cmap, hold=True,
            cbar=None, lonra=lonra, latra=latra,
            unit=r"$-2 \Delta \ln (L)$",
            )

        fig = plt.gcf()
        ax = plt.gca()
        image = ax.get_images()[0]
        # Place colorbar by hand
        cb = fig.colorbar(image, ax=ax, orientation='horizontal', aspect=50)
        cb.ax.xaxis.set_label_text(r"$-2 \Delta \ln (L)$")

        # Plot the best-fit location
        # This requires some more coordinate transformations
        healpy.projplot(np.pi/2 - minDec, minRA,
            '*', ms=5, label=r'scan best fit', color='black', zorder=2)

        # Plot the contours
        contour_areas=[]
        for contour_level, contour_label, contour_color, contours in zip(contour_levels,
            contour_labels, contour_colors, contours_by_level):
            contour_area = 0.
            for contour in contours:
                _ = contour.copy()
                _[:,1] += np.pi-np.radians(ra)
                _[:,1] %= 2*np.pi
                contour_area += self.calculate_area(_)
            contour_area_sqdeg = abs(contour_area) * (180.*180.)/(np.pi*np.pi) # convert to square-degrees
            contour_areas.append(contour_area_sqdeg)
            contour_label = contour_label + ' - area: {0:.2f} sqdeg'.format(
                contour_area_sqdeg)
            first = True
            for contour in contours:
                theta, phi = contour.T
                if first:
                    healpy.projplot(theta, phi, linewidth=2, c=contour_color,
                        label=contour_label)
                else:
                    healpy.projplot(theta, phi, linewidth=2, c=contour_color)
                first = False

        # Add some grid lines
        healpy.graticule(dpar=2, dmer=2, force=True)

        # Set some axis limits
        lower_ra = minRA + np.radians(lonra[0])
        upper_ra = minRA + np.radians(lonra[1])
        lower_dec = minDec + np.radians(latra[0])
        upper_dec = minDec + np.radians(latra[1])

        lower_lon = np.degrees(lower_ra)
        upper_lon = np.degrees(upper_ra)
        tmp_lower_lat = np.degrees(lower_dec)
        tmp_upper_lat = np.degrees(upper_dec)
        lower_lat = min(tmp_lower_lat, tmp_upper_lat)
        upper_lat = max(tmp_lower_lat, tmp_upper_lat)

        # Label the axes
        hp_ticklabels(zoom=True, lonra=lonra, latra=latra,
            rot=(lon,lat,0),
            bounds=(lower_lon, upper_lon, lower_lat, upper_lat))

        if plot_4fgl:
            # Overlay 4FGL sources
            plot_catalog(equatorial_map, cmap, lower_ra, upper_ra, lower_dec, upper_dec)

        # Approximate contours as rectangles
        ra = minRA * 180./np.pi
        dec = minDec * 180./np.pi
        for l, contours in enumerate(contours_by_level[:2]):
            ra_plus = None
            theta, phi = np.concatenate(contours).T
            ra_plus, ra_minus, dec_plus, dec_minus = bounding_box(ra, dec, theta, phi)
            contain_txt = "Approximating the {0}% error region as a rectangle, we get:".format(["50", "90"][l]) + " \n" + \
                          "\t RA = {0:.2f} + {1:.2f} - {2:.2f}".format(
                              ra, ra_plus, np.abs(ra_minus)) + " \n" + \
                          "\t Dec = {0:.2f} + {1:.2f} - {2:.2f}".format(
                              dec, dec_plus, np.abs(dec_minus))
            print(contain_txt)
        if plot_bounding_box:
            bounding_ras_list, bounding_decs_list = [], []
            # lower bound
            bounding_ras_list.extend(list(np.linspace(ra+ra_minus,
                ra+ra_plus, 10)))
            bounding_decs_list.extend([dec+dec_minus]*10)
            # right bound
            bounding_ras_list.extend([ra+ra_plus]*10)
            bounding_decs_list.extend(list(np.linspace(dec+dec_minus,
                dec+dec_plus, 10)))
            # upper bound
            bounding_ras_list.extend(list(np.linspace(ra+ra_plus,
                ra+ra_minus, 10)))
            bounding_decs_list.extend([dec+dec_plus]*10)
            # left bound
            bounding_ras_list.extend([ra+ra_minus]*10)
            bounding_decs_list.extend(list(np.linspace(dec+dec_plus,
                dec+dec_minus,10)))
            # join end to beginning
            bounding_ras_list.append(bounding_ras_list[0])
            bounding_decs_list.append(bounding_decs_list[0])

            bounding_ras: np.ndarray = np.asarray(bounding_ras_list)
            bounding_decs: np.ndarray = np.asarray(bounding_decs_list)
            bounding_phi = np.radians(bounding_ras)
            bounding_theta = np.pi/2 - np.radians(bounding_decs)
            bounding_contour = np.array([bounding_theta, bounding_phi])
            bounding_contour_area = 0.
            bounding_contour_area = abs(self.calculate_area(bounding_contour.T))
            bounding_contour_area *= (180.*180.)/(np.pi*np.pi) # convert to square-degrees
            contour_label = r'90% Bounding rectangle' + ' - area: {0:.2f} sqdeg'.format(
                bounding_contour_area)
            healpy.projplot(bounding_theta, bounding_phi, linewidth=0.75,
                c='r', linestyle='dashed', label=contour_label)

        # Output contours in RA, dec instead of theta, phi
        saving_contours: list = []
        for contours in contours_by_level:
            saving_contours.append([])
            for contour in contours:
                saving_contours[-1].append([])
                theta, phi = contour.T
                ras = phi
                decs = np.pi/2 - theta
                for tmp_ra, tmp_dec in zip(ras, decs):
                    saving_contours[-1][-1].append([tmp_ra, tmp_dec])

        # Save the individual contours, send messages
        for i, val in enumerate(["50", "90"]):
            ras = list(np.asarray(saving_contours[i][0]).T[0])
            decs = list(np.asarray(saving_contours[i][0]).T[1])
            tab = {"ra (rad)": ras, "dec (rad)": decs}
            savename = unique_id + ".contour_" + val + ".txt"
            try:
                print("Dumping to", savename)
                ascii.write(tab, savename, overwrite=True)
            except OSError as err:
                print("OS Error prevented contours from being written, maybe a memory issue.")
                print(err)

        uncertainty = [(ra_minus, ra_plus), (dec_minus, dec_plus)]
        fits_header = format_fits_header(
            (event_metadata.run_id, event_metadata.event_id, event_metadata.event_type),
            0,
            np.degrees(minRA),
            np.degrees(minDec),
            uncertainty,
        )
        mmap_nside = healpy.get_nside(equatorial_map)

        # Plot the original online reconstruction location
        if np.sum(np.isnan([extra_ra, extra_dec, extra_radius])) == 0:

            def circular_contour(ra, dec, sigma, nside):
                """For plotting circular contours on skymaps ra, dec, sigma all
                expected in radians."""
                dec = np.pi/2. - dec
                sigma = np.rad2deg(sigma)
                delta, step, bins = 0, 0, 0
                delta= sigma/180.0*np.pi
                step = 1./np.sin(delta)/10.
                bins = int(360./step)
                Theta = np.zeros(bins+1, dtype=np.double)
                Phi = np.zeros(bins+1, dtype=np.double)
                # define the contour
                for j in range(0,bins) :
                    phi = j*step/180.*np.pi
                    vx = np.cos(phi)*np.sin(ra)*np.sin(delta) + np.cos(ra)*(np.cos(delta)*np.sin(dec) + np.cos(dec)*np.sin(delta)*np.sin(phi))
                    vy = np.cos(delta)*np.sin(dec)*np.sin(ra) + np.sin(delta)*(-np.cos(ra)*np.cos(phi) + np.cos(dec)*np.sin(ra)*np.sin(phi))
                    vz = np.cos(dec)*np.cos(delta) - np.sin(dec)*np.sin(delta)*np.sin(phi)
                    idx = healpy.vec2pix(nside, vx, vy, vz)
                    DEC, RA = healpy.pix2ang(nside, idx)
                    Theta[j] = DEC
                    Phi[j] = RA
                Theta[bins] = Theta[0]
                Phi[bins] = Phi[0]
                return Theta, Phi

            # dist = angular_distance(minRA, minDec, extra_ra * np.pi/180., extra_dec * np.pi/180.)
            # print("Millipede best fit is", dist /(np.pi * extra_radius/(1.177 * 180.)), "sigma from reported best fit")
        

            extra_ra_rad = np.radians(extra_ra)
            extra_dec_rad = np.radians(extra_dec)
            extra_radius_rad = np.radians(extra_radius)
            extra_lon = extra_ra_rad
            extra_lat = extra_dec_rad

            healpy.projscatter(np.degrees(extra_lon), np.degrees(extra_lat),
                lonlat=True, c='m', marker='x', s=20, label=r'Reported online (50%, 90%)')
            for cont_lev, cont_scale, cont_col, cont_sty in zip(['50', '90.'], 
                    [1., 2.1459/1.177], ['m', 'm'], ['-', '--']):
                spline_contour = circular_contour(extra_ra_rad, extra_dec_rad,
                    extra_radius_rad*cont_scale, healpy.get_nside(equatorial_map))
                spline_lon = spline_contour[1]
                spline_lat = np.pi/2. - spline_contour[0]
                healpy.projplot(np.degrees(spline_lon), np.degrees(spline_lat), 
                    lonlat=True, linewidth=2., color=cont_col, 
                    linestyle=cont_sty)

        plt.legend(fontsize=6, loc="lower left")

        # For vertical events, calculate the area with the number of pixels
        # In the healpy map   
        for lev in contour_levels[1:2]:
            area_per_pix = healpy.nside2pixarea(healpy.get_nside(equatorial_map))
            num_pixs = np.count_nonzero(equatorial_map[~np.isnan(equatorial_map)] < lev)
            healpy_area = num_pixs * area_per_pix * (180./np.pi)**2.
        print("Contour Area (90%):", contour_areas[1], "degrees (cartesian)",
            healpy_area, "degrees (scaled)")


        # Dump the whole contour
        path = unique_id + ".contour.pkl"
        print("Saving contour to", path)
        with open(path, "wb") as f:
            pickle.dump(saving_contours, f)

        healpy.write_map(f"{unique_id}.skymap_nside_{mmap_nside}.fits.gz",
            equatorial_map, coord = 'C', column_names = ['2LLH'],
            extra_header = fits_header, overwrite=True)

        # Save the figure
        print("saving: {0}...".format(plot_filename))
        #ax.invert_xaxis()
        fig.savefig(plot_filename, dpi=dpi, transparent=True)

        print("done.")

        savename = plot_filename[:-4] + ".png"
        print(savename)

        plt.close()
