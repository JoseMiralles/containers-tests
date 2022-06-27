
from typing import Callable

def say_hello() -> None:
    """
    Says hello
    """
    print("Hello!")

def average (*numbers: float) -> float:
    """Defines the average of the given parameters"""
    return sum(numbers) / len(numbers)

def sayHelloToPerson(name: str = "Nameless") -> None:
    print(f"Hello {name}!")


# Using parameter keywords on invocation
sayHelloToPerson(name="Jose")


# Anonymous Functions
toUpper: Callable[[str], str] = lambda s: s.upper()

# Can be spread across multiple lines
toUpperTwo: Callable[[str, str], str] = (
    lambda s, s2:
        s + s2.upper())


# Undefined number of parameters. EX: my_func(1,3,4,...)
## The arguments are taken as a tuple.
def prepend_strings(prepend: str, *strings: str) -> str:
    return " ".join(map(lambda _s: prepend + _s, strings))

print(prepend_strings("le ", "Paris", "Corn", "House"))


# Undefined number of key value pairs parameters: EX: my_func()
## The arguments are taken as a dictionary
def welcome_people(
    greeting: str,
    **_names_cities: str) -> None:
    for _name, _city in _names_cities.items():
        print(f"{greeting},", _name, "from", _city)

welcome_people("Hello", Jose="Guatemala", Lil_John="Atlanta")


# PARAMETER ORDER
## 1. formal positional arguments
## 2. *args
## 3. Keyword arguments with default values
## 4. **kwargs

def my_func(arg_1: str, arg_2: str, *args: int, arg_3:str="hi", arg_4:str="hello", **dictionary:str)->None:
    pass
