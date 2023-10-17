try:
    from .version import __version__
except ModuleNotFoundError:
    from importlib_metadata import version as _get_version

    __version__ = _get_version("synthesized3")

import warnings  # pylint: disable=wrong-import-position

warnings.warn(
    "This is a pre-release version of synthesized SDK3, "
    "which has a different API to SDK2 and is still under development. "
    "Please run 'pip install \"synthesized < 3\"' to use the latest stable "
    "version with all of the features."
)

from synthesized3.utils import warnings_utils  # pylint: disable=wrong-import-position

warnings_utils.apply_third_party_warnings_env_var()  # before any other synthesized3 imports

from .column_type import ColumnType  # pylint: disable=wrong-import-position
from .data_interface import (  # pylint: disable=wrong-import-position
    PandasDataInterface,
    SparkDataInterface,
)
from .nature import Nature  # pylint: disable=wrong-import-position
from .synthesizer import TableSynthesizer  # pylint: disable=wrong-import-position

__all__ = [
    "PandasDataInterface",
    "TableSynthesizer",
    "SparkDataInterface",
    "ColumnType",
    "Nature",
]
