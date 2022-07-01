# pipenv

## Enviroment variables
`.profile`
```
...
# Setup Python virtual enviroment variables
export PIPENV_VENV_IN_PROJECT=1
export PYENV_ROOT=$HOME/.PYENV
export PIPENV_PYTHON=PYPENV_ROOT/SHIMS/PYTHON
export PATH="$PYPENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"

eval "(pyenv init -)"
```

## Create virtual enviroment with pipenv
1. Create and navigate to a new directory for your new project.
1. `pipenv install --python "$PYENV_ROOT/versions/3.8.1/bin/python"`
    - This creates a `Pipfile` and a `Pipfile.lock` file, as well as a `.venv` directory.
    - use `pyenv versions` to see installed versions.
1. `pipenv shell` activates the current enviroment