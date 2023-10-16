from __future__ import annotations

import os
import subprocess

from pathlib import Path

import pytest

from pytest_gitconfig import GitConfig


def assert_config(key: str, expected: str):
    __tracebackhide__ = True
    assert (
        subprocess.check_output(f"git config {key}", shell=True).strip().decode("utf-8") == expected
    )


@pytest.mark.mypy_testing
def test_gitconfig(gitconfig: GitConfig):
    assert gitconfig.path != Path("~/.gitconfig")
    assert str(gitconfig) == str(gitconfig.path)
    assert os.environ["GIT_CONFIG_GLOBAL"] == str(gitconfig.path)


@pytest.mark.mypy_testing
def test_gitconfig_set_dotted_kwargs(gitconfig: GitConfig):
    expected = "new name"
    gitconfig.set(**{"user.name": expected})

    assert_config("user.name", expected)


@pytest.mark.mypy_testing
def test_gitconfig_set_dict_kwargs(gitconfig: GitConfig):
    expected = "new name"
    gitconfig.set(user={"name": expected})

    assert_config("user.name", expected)


@pytest.mark.mypy_testing
def test_gitconfig_set_dict(gitconfig: GitConfig):
    expected = "new name"
    gitconfig.set({"user.name": expected})

    assert_config("user.name", expected)


@pytest.mark.mypy_testing
def test_gitconfig_set_nested_dicts(gitconfig: GitConfig):
    expected = "new name"
    gitconfig.set({"user": {"name": expected}})

    assert_config("user.name", expected)
