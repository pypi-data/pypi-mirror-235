"""Python post processing integrations for the Fluent solver."""

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

_VERSION_INFO = "Build date: October 17, 2023 12:40 UTC ShaID: b7d3620"
__version__ = importlib_metadata.version(__name__.replace(".", "-"))


def version_info() -> str:
    """Method returning the version of PyFluent being used.
    Returns
    -------
    str
        The PyFluent version being used.
    Notes
    -------
    Only available in packaged versions. Otherwise it will return __version__.
    """
    return _VERSION_INFO if _VERSION_INFO is not None else __version__


from ansys.fluent.visualization._config import get_config, set_config  # noqa: F401
