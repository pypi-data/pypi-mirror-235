# pytest-gitconfig

[![CI](https://github.com/noirbizarre/pytest-gitconfig/actions/workflows/ci.yml/badge.svg)](https://github.com/noirbizarre/pytest-gitconfig/actions/workflows/ci.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/noirbizarre/pytest-gitconfig/main.svg)](https://results.pre-commit.ci/latest/github/noirbizarre/pytest-gitconfig/main)
[![PyPI](https://img.shields.io/pypi/v/pytest-gitconfig)](https://pypi.org/project/pytest-gitconfig/)
[![PyPI - License](https://img.shields.io/pypi/l/pytest-gitconfig)](https://pypi.org/project/pytest-gitconfig/)
[![codecov](https://codecov.io/gh/noirbizarre/pytest-gitconfig/branch/main/graph/badge.svg?token=OR4JScC2Lx)](https://codecov.io/gh/noirbizarre/pytest-gitconfig)

Provide a gitconfig sandbox for testing

## Getting started

Install `pytest-gitconfig`:

```shell
# pip
pip install pytest-gitconfig
# pipenv
pipenv install pytest-gitconfig
# PDM
pdm add pytest-gitconfig
```

Then the `default_gitconfig` session fixture will be automatically loaded for the session
providing isolation from gloval user defined values.

If you want to customize or depend on it

```python
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from pytest_gitconfig import GitConfig

@pytest.fixture
def default_git_user_name() -> str:
  return "John Doe"

@pytest.fixture(scope="session", autouse=True)
def fixture_depending_on_default_gitconfig(default_gitconfig: GitConfig) -> Whatever:
    # You can set values, the following statements are equivalents
    default_gitconfig.set({"some": {key: value}}) # nested dicts form
    default_gitconfig.set({"some.key": value})    # dict with dotted keys form
    # Or read them
    data = default_gitconfig.get("some.key")
    data = default_gitconfig.get("some.key", "fallback")
    # If you need the path to the gitconfig file
    assert str(default_gitconfig) == str(default_gitconfig.path)
    return whatever
```

Note that the `default_gitconfig` fixture being session-scoped (avoiding the performance hit of creating a gitconfig file for each test),
set values are persistent for the whole session and should be defined once preferably in your `conftest.py`.
But if you need to temporarily override some value, you can use the `override()` context manager which is accepting the same parameters as `set()`.

This allows to override it directly during a test:

```python
from __future__ import annotations
from typing import TYPE_CHECKING, Iterator

if TYPE_CHECKING:
  from pytest_gitconfig import GitConfig


def test_something(default_gitconfig):
    with gitconfig.override({"other.key": value}):
        # Do something depending on those overridden values
```

But to test some value in some specific tests, its best to rely on `gitconfig` which is providing a function-scoped GitConfig:

```python
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from pytest_gitconfig import GitConfig


def test_something(gitconfig: GitConfig):
    gitconfig.set({"other.key": value})  # Only valid for this test
    # Do something depending on those overridden values
```

A classical setup being:

- default to using the session-scoped `default_gitconfig` to ensure isolation.
- some specific test cases relying on some specific settings set on the `gitconfig` function-scoped fixture

This has the following benefits:

- session isolation is done only once
- test having specific settings does not impact other tests
- test having specific settings can be run in parallel

## Provided fixtures

### Function-scoped

#### `gitconfig -> pytest_gitconfig.GitConfig`

This is the main fixture which is creating a new and clean git config file for the tested function.

It inherit from `default_gitconfig` (meaning that all values set on `default_gitconfig` will be set on `gitconfig`)

It works by monkeypatching the `GIT_CONFIG_GLOBAL` environment variable.
So, if you rely on this in a context where `os.environ` is ignored, you should patch it yourself using this fixture.

#### `git_user_name -> str | None`

Provide the initial `user.name` setting for `gitconfig`.
If `None`, `user.name` will inherit its value from `default_config`,
so most probably from `default_git_user_name` if not overridden.

#### `git_user_email -> str | None`

Provide the initial `user.email` setting for `gitconfig`.
If `None`, `user.email` will inherit its value from `default_config`,
so most probably from `default_git_user_email` if not overridden.

#### `git_init_default_branch -> str | None`

Provide the initial `init.defaultBranch` setting for `gitconfig`.
If `None`, `init.defaultBranch` will inherit its value from `default_config`,
so most probably `default_git_init_default_branch` if not overridden.

### Session-scoped

#### `defalt_gitconfig -> pytest_gitconfig.GitConfig`

This is the main fixture which is creating a new and clean git config file for the test session.
It is loaded automatically if you have `pytest-gitconfig` installed.

By default, it will set 3 settings:

- `user.name`
- `user.email`
- `init.defaultBranch`

It works by monkeypatching the `GIT_CONFIG_GLOBAL` environment variable.
So, if you rely on this in a context where `os.environ` is ignored, you should patch it yourself using this fixture.

#### `default_git_user_name -> str`

Provide the initial `user.name` setting. By default `pytest_gitconfig.DEFAULT_GIT_USER_NAME`.
Override to provide a different initial value.

#### `default_git_user_email -> str`

Provide the initial `user.email` setting. By default `pytest_gitconfig.DEFAULT_GIT_USER_EMAIL`.
Override to provide a different initial value.

#### `default_git_init_default_branch -> str`

Provide the initial `init.defaultBranch` setting. By default `pytest_gitconfig.DEFAULT_GIT_BRANCH` (`main`).
Override to provide a different initial value.

#### `sessionpatch -> pytest.MonkeyPatch`

A `pytest.MonkeyPatch` session instance.

## API

### `pytest_gitconfig.GitConfig`

An object materializing a given `gitconfig` file.

#### `set(self, data: Mapping[str, Any])`

Write some `gitconfig` values.
It accepts a `dict` of parsed data sections as dict or dotted-key-values.

#### `get(self, key: str, default: Any = _UNSET)`

Get a setting given its dotted key. Get a 2nd default value. Raise `KeyError` if config does not exists and `default` is not provided

#### `override(self, data: Mapping[str, Any]) -> Iterator[GitConfig]`

A context manager setting the values and restoring them on exit.
Accept the same format a the `set()` method.
