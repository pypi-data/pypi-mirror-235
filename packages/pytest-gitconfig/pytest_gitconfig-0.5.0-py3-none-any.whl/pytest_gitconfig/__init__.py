from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files  # type: ignore[no-redef,import-not-found]

from .plugin import (
    DEFAULT_GIT_BRANCH,
    DEFAULT_GIT_USER_EMAIL,
    DEFAULT_GIT_USER_NAME,
    GitConfig,
)


def read_version() -> str:
    try:
        return version("pytest-gitconfig")
    except (PackageNotFoundError, ImportError):
        version_file = files(__package__) / "VERSION"
        return version_file.read_text() if version_file.is_file() else "0.0.0.dev"


__version__ = read_version()
