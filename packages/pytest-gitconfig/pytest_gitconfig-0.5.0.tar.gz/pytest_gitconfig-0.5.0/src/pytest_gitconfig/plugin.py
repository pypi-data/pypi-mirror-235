from __future__ import annotations

import os

from configparser import ConfigParser
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator, Mapping, overload

import pytest

DEFAULT_GIT_USER_NAME = "Pytest"
DEFAULT_GIT_USER_EMAIL = "pytest@local.dev"
DEFAULT_GIT_BRANCH = "main"


@pytest.fixture(scope="session")
def sessionpatch() -> Iterator[pytest.MonkeyPatch]:
    with pytest.MonkeyPatch.context() as mp:
        yield mp


@pytest.fixture(scope="session")
def git_user_name() -> str:
    return DEFAULT_GIT_USER_NAME


@pytest.fixture(scope="session")
def git_user_email() -> str:
    return DEFAULT_GIT_USER_EMAIL


@pytest.fixture(scope="session")
def git_init_default_branch() -> str:
    return DEFAULT_GIT_BRANCH


@dataclass
class GitConfig:
    path: Path

    def __str__(self):
        return str(self.path)

    @overload
    def set(self, data: Mapping[str, Any]):
        ...

    @overload
    def set(self, **kwargs: Any):
        ...

    def set(self, data: Mapping[str, Any] | None = None, **kwargs: Any):
        cfg = self._read()
        for section, option, value in self._iter_data(data or kwargs):
            if not cfg.has_section(section):
                cfg.add_section(section)
            cfg.set(section, option, value)
        self._write(cfg)

    def get(self, key) -> str:
        cfg = self._read()
        section, option = self._parse_key(key)
        return cfg[section][option]

    def _iter_data(self, data: Mapping[str, Any]) -> Iterator[tuple[str, str, str]]:
        for key, content in data.items():
            if "." in key:
                # Dotted key
                section, option = key.split(".", 1)
                yield section, option, content
            else:
                # Nested dicts
                for option, value in content.items():
                    yield key, option, value

    def _parse_key(self, key: str) -> list[str]:
        return key.rsplit(".", 1)

    def _read(self) -> ConfigParser:
        cfg = ConfigParser()
        cfg.read(self.path)
        return cfg

    def _write(self, cfg: ConfigParser):
        with self.path.open("w") as out:
            cfg.write(out)


@pytest.fixture(scope="session")
def gitconfig(
    tmp_path_factory: pytest.TempPathFactory,
    sessionpatch: pytest.MonkeyPatch,
    git_user_name: str,
    git_user_email: str,
    git_init_default_branch: str,
) -> GitConfig:
    path = tmp_path_factory.mktemp("git", False) / "config"
    gitconfig = GitConfig(path)

    for var in os.environ:
        if var.startswith("GIT_"):
            sessionpatch.delenv(var, False)
    sessionpatch.setenv("GIT_CONFIG_GLOBAL", str(gitconfig))

    settings: dict[str, Any] = {
        "user.name": git_user_name,
        "user.email": git_user_email,
        "init.defaultBranch": git_init_default_branch,
    }

    gitconfig.set(**settings)

    return gitconfig
