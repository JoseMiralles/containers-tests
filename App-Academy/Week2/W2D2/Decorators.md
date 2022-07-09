# Decorators

## Introspection
```
print(dir(say_hi))
# ['__annotations__', '__call__', ...]
```

## Callbacks
Python supports callbacks.

```
def parent_function(call_back: Callable[[str, str], None]) -> None:
    # do stuff
    call_back("one", "two")

parent_function(lambda s1,s2: print(s1,s2))
```

## Inner functions
Functions can return other functions, and apply the concept of curring.
```
def outer_function(str: phrase1) -> Callable[[str], None]:
    def inner_function(phrase2: str) -> None:
        print(phrase1, phrase2)
    return inner_function
```

<br>

## Decorators

This is the concept of wrapping a function with another function

```
def message_decorator(message_func: Callable[[], str]) -> Callable[[str], None]:
    def message_wrapper(name: str) -> None:
        print(message_func() + "This is a message from " + name)
    return message_wrapper

def say_hi() -> str:
    return "Hi! "

say_hi = message_decorator(say_hi) # Wrap this function
print(say_hi("Jose")) # Hi! This is a message from Jose
```

Instead of having to write `say_hi = message_decorator(say_hi)`, we can use the decorator flag.

```
...
@message_decorator
def say_hi():
    return "Hi!"

print(say_hi("Jose")) # Hi! This is a message from Jose
```

<br>

Here is an example that allow the decorated function `say_hi` to take arguments:

```
from typing import Callable


def message_decorator(message_func: Callable[[str], str]) -> Callable[[str, str], None]:
    def message_wrapper(name: str, author: str) -> None:
        print(message_func(name) + "This is a message from " + author)
    return message_wrapper

@message_decorator
def say_hi(name: str) -> str:
    return "Hi! "

print(say_hi("Jose", "Pitbull")) # Hi! This is a message from Jose
```

<br>

## Some built in class method decorators

```
@property
@classmethod
@staticmethod
@property
```
<br>

## Custom class decorators

Classes can also have decorators.

https://levelup.gitconnected.com/mastering-decorators-in-python-3-588cb34fff5e#:~:text=I%20love%20it.-,Class%20Decorators,-A%20class%20decorator