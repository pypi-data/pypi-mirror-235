# noqa: D200,D212,D400,D415
"""
.. include:: ../../README.md
"""  # noqa: RST499
# stdlib
import logging

# local
from pyspry.base import Settings
from pyspry.nested_dict import NestedDict

__all__ = ["__version__", "NestedDict", "Settings"]

__version__ = "1.1.0b1"

_logger = logging.getLogger(__name__)
_logger.debug(
    "the following classes are exposed for this package's public API: %s",
    ",".join([Settings.__name__, NestedDict.__name__]),
)
