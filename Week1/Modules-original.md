
# Modules

## Terms

- **Module**: A folder or file with Python code.
- **Package**: Directory with multiple modules.
- *__init__.py*: The default file for a package.
- **Submodule**: A file in a module folder.

## Visualization
```
project
│   README.md
│   __init__.py
|   shopping_cart.py         <== module
│
└───pet                      <== package
│   │
│   └───mammal               <== module (and package)
|   |   |   __init__.py
│   |   │   dog.py           <== submodule
│   |   │   cat.py           <== submodule
│   |   │   ...
│   │
│   └───fish                 <== module (and package)
|   |   |   __init__.py
│   │
│   └───bird                 <== module (and package)
|       |   __init__.py
│
└───housing                  <== module (and package)
    │   __init__.py
    │   aquarium.py          <== submodule
    │   cage.py              <== submodule
    │   kennel.py            <== submodule
    |   ...
```

# Import Statements
```
- import <module> - most basic
- import <package>.<subpackage>.<module> - dot syntax
- from <package> import <module> - one module in a package
- from <package> import <module>, <module> - multiple modules or submodules in a package
- from . import <submodule>- special case for module's __init__.py to get submodules in the same folder
- from <module> import <function>, <function> - down to the function level
- from <package> import <module> as <altName> - renaming to avoid confusion or conflict
```

## Elegant Example:
```
from urllib.request import (
  HTTPDefaultErrorHandler as ErrorHandler,
  HTTPRedirectHandler as RedirectHandler,
  Request,
  pathname2url,
  url2pathname,
  urlopen,
)
```