"""
This module provides a mechanism for obtaining the version of the current Python package using
importlib.metadata or importlib_metadata, depending on the Python version.

It retrieves the package version using the appropriate method and assigns it to the '__version__'
attribute if available, falling back to "unknown" if the version cannot be found.

Usage:
    Import this module to access the '__version__' attribute representing the package version.

Compatibility:
    - Requires Python 3.8 or later for 'importlib.metadata'.
    - For Python versions prior to 3.8, 'importlib_metadata' is used.

Note:
    - This module handles the compatibility between different Python versions to ensure that
      '__version__' is set correctly.
"""
import sys

if sys.version_info[:2] >= (3, 8):
    from importlib.metadata import PackageNotFoundError  # pragma: no cover
    from importlib.metadata import version
else:
    from importlib_metadata import PackageNotFoundError  # pragma: no cover
    from importlib_metadata import version

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
