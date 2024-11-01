# Development Environment

## Docker

Set up for development using docker, docker-compose, and buildx.

```
pacman -S docker docker-buildx docker-compose
```

## NodeJS

No NVM locally for now. Most development to be done in docker.

```
pacman -S nodejs npm
```

### Quick Start for Node

WIP

## Python

Use the rolling release `python` in arch repo, python version management using
`pyenv`, and environment management using `poetry`.

```
pacman -S python pyenv poetry
```

Configure poetry to create `.venv` directories in project directories, instead
of hiding it somewhere.
```
poetry config virtualenvs.in-project true
poetry config --list
```

### Quick Start for Python

* Create project directory and `cd` into it.
* Set up a suitable python version for the project, managed by pyenv.
    ```
    pyenv install --list
    pyenv install 3.11.9
    pyenv local 3.11.9
    ```
* Set up poetry project, specifying a python version. Otherwise poetry will
  default to the system's python.
    ```
    poetry init --python ^3.11.9 --no-interaction
    ```
* Specify the python version for poetry to use for this project.
    ```
    poetry env use $(pyenv which python)
    ```
* Ensure poetry is using this python version.
    ```
    poetry run python --version
    ```

# Rust

* Use `pacman` to install `rustup`.
    ```
    pacman -S rustup
    ```
* Use `rustup` to install `rustc` and `cargo`. Follow official guides.

# Python (NEW)

* Consider migrating out of more complex `poetry` and `pyenv` workflow.
* Use `pacman` to install `uv`.
    ```
    pacman -S uv
    ```
* Manage python projects using uv. Follow official guides.
* `uv` takes care of:
    * python versions
    * virtual environments
    * dependencies
    * etc?

