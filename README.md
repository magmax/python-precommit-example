# About this repository

This repository is just to show how [pre-commit](https://pre-commit.com/) works.

How to use it:

1. Clone this repository. Forking it is not required, because we will work just
   with `commit`; no `push` is required.
1. Install pre-commit. Example: `pip install -t . pre-commit`
1. Install the pre-commit hooks: `pre-commit install`
1. Modify the `example.py` program. Add a couple of line feeds, for example.
1. Do commit. Example: `git commit -am "update"`
1. It should fail. You can check what has happened with `git diff`.
1. Do commit again. It should work now.

# Why?

The first execution runs [black](https://github.com/psf/black), fixing the code.
The second run finds the code fixed so it works.

# Remember that:

- pre-commit will only check modified files.
- file `.pre-commit-config.yaml` contains the pre-commit configuration.
- `black` will use 120 character lines. So, file `.flake8` is required to run
  the `flake8` pre-commit plugin.
