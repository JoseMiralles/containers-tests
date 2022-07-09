# Packages and Modules

## Two kinds of modules
- Directory modules need to have a `__init__.py` file.
- Invokable modules need to have a `__main__.py` file.
- Files are also modules.

## Two ways of invoking modules
- As a script: `python my_package/my_module.py`
- As a module: `python -m my_package.my_module`

## Invoking directories
Directories / packages can also be invoked as long as they have `__init__.py` and `__main__.py` files.
- `python my_package` This required a `__main__.py`

## All init files are invoked when a subpackage or submodule is imported.

For example, if a package is imported as such: `import my_package.subpackage.module2`, then the relevant `__init__.py` file is executed.
```
|--my_package/
   |-- __init.py__          <- This is executed
   |-- __main.py__
   |-- module1.py
   |-- subpackage/
        |-- __init__.py     <- This is executed
        |-- module1.py
        |-- module2.py      <- We are importing this
```


