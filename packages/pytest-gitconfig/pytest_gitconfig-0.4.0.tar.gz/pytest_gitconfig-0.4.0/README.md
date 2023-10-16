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

Then in your `conftest.py`:

```python
# All tests are using the sandboxed gitconfig
pytestmark = pytest.mark.usefixtures("gitconfig")
```

or if you want to customize or depend on it

```python
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from pytest_gitconfig import GitConfig

@pytest.fixture
def git_user_name() -> str:
  return "John Doe"

@pytest.fixture
def fixture_depending_on_gitconfig(gitconfig: GitConfig) -> Whatever:
    # You can set values
    gitconfig.set(group={key: value})  # nested key-value form
    gitconfig.set(**{"othersome.key": True})  # dotted keys form
    # Or read them
    data = gitconfig.get("path.to.key")
    # If you need the path to the gitconfig file
    GIT_CONFIG_GLOBAL = str(gitconfig)
    return whatever
```

## Provided fixtures

All fixtures are session-scoped.

### `gitconfig -> pytest_gitconfig.GitConfig`

This is the main fixture which is creating a new and clean git config file for the test session.

By default, it will set 3 settings:

- `user.name`
- `user.email`
- `init.defaultBranch`

The fixture when required provide a `pytest_gitconfig.GitConfig` object with the following methods:

- `gitconfig.set()` accepting either a `dict` with the parsed data sections or key-values with dotted key names.
- `gitconfig.get()` to get a setting given its dotted key.

It works by monkeypatching the `GIT_CONFIG_GLOBAL` environment variable.
So, if you rely on this in a context where `os.environ` is ignored, you should patch it yourself using this fixture.

### `git_user_name -> str`

Provide the initial `user.name` setting. By default `pytest_gitconfig.DEFAULT_GIT_USER_NAME`.
Override to provide a different initial value.

### `git_user_email -> str`

Provide the initial `user.email` setting. By default `pytest_gitconfig.DEFAULT_GIT_USER_EMAIL`.
Override to provide a different initial value.

### `git_init_default_branch -> str`

Provide the initial `init.defaultBranch` setting. By default `pytest_gitconfig.DEFAULT_GIT_BRANCH` (`main`).
Override to provide a different initial value.

### `sessionpatch -> pytest.MonkeyPatch`

A `pytest.MonkeyPatch` session instance.
