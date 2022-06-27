from typing import Any, List, Literal, Set, TypedDict, Tuple, Dict, Union


# LISTS

empty_list: List[int] = []
departments_list: List[str] = ["HR", "Development", "Sales", "Finances"]
other_empty_list: List[str] = list()

is_sales_in_list: bool = "Sales" in departments_list


# TUPLES
time_blocks: Tuple[str, str] = ('AM', 'PM')
large_tuple: Tuple[str, ...] = ("one", "two", "three", "four")


# RANGE - an inmutable collection of numbers
my_range: range = range(1, 5)
multiples_of_five: range = range(0,20,5) # -> [0, 5, 10, 15], 20 is not included
negative_multiples_of_five: range = range(0,20,-5) # -> [0, -5, -10, -15], -20 is not included

for i in range(0, 10):
    pass


# DICTIONARY
class User(TypedDict): # Similar to a type or interface in Typescript
    name: str
    level: Literal[1,2,3]
    comments: List[str]

users: Dict[str,User] = {
    "1": {"name": "Jose", "level": 2, "comments": []},
    "2": {"name": "spiderman", "level": 2, "comments": []}
}

cats_age: Dict[str,int] = dict(pete=1, mike=2)

complex_dict: Dict[str, Any] = { # It is better to use a class which extends TypedDict
    "name": "Jose",
    "week_days": ["Monday", "Friday"]
}

## Get keys from dictionary
for _key in cats_age.keys():
    print(_key)
# It is prefered to iterate trough the dictionary instead of calling keys()
for _key,_val in cats_age.items():
    print(_key, _val)

for _val in cats_age.values():
    print(_val)

# SETS
visited: Set[int] = {1, 3, 6}
visited.add(5)

favorites: Set[str] = set()
favorites.add("Pie")

united_set: Set[Union[str,int]] = visited | favorites
intersections = {1,2,3} | {2,3,4} # -> {2,3}
removed_diferents = {1,2,3} - {1,2} # -> {3}
symmetric_differences = {1,2,3} ^ {2,4,6} # -> {1,3,4,6}

# Built-in functions
numbers: List[int] = [1,2,3,4]

under_3 = filter(lambda n: n < 3, numbers)


## Mapping
def _map_func(_number: int) -> int:
    if _number == 1:
        return 2
    return _number**2

mapped_numbers = map(_map_func, numbers)

print(f"Type of mapped_numbers: {type(mapped_numbers)}")

for _num in mapped_numbers:
    print(_num)


## Sorting

names: Tuple[str, ...] = ("Jose", "Enrique", "Lil John")
sortedNames: List[str] = sorted(names, key=str.lower, reverse=False)
# Key is used to define an operation that should happen for each item before it is compared.
# In this case, key is used to turn the item to lowercase before they are compared.

### Custom Sorting
# Example: Sort users by the length of their name

def _user_sort_func(_user: User)->int:
    return len(_user["name"])

user_list: List[User] = List(users.values())

sorted_users = sorted(user_list, key=_user_sort_func)



## Enumeration, converts items to a series of tuples
enumerated = enumerate(names, start=2) # -> (2, "Jose"), (3, "Enrique"), ...


## Zip - aggregate collections into tuples
zipped = zip(names, sortedNames) # -> ('Jose', 'Enrique'), ('Enrique', 'Jose'), ('Lil John', 'Lil John')
for _tup in zipped:
    print(_tup)


# OTHERS
LENGTH = len(names)
max_number = max(2,4,7,6, key=None) # Can also take a collection
min_number = min( (2,5,7,3,2), key=None )
total_sum = sum((3,5,6,32))

are_any_items_truthy = any((0,0,0,3,0)) # True because of the 3
are_all_items_truthy = all((3,6,8,0)) # False because of the 0

## Loop trought attributes in object
for _attr in dir(User(name="Jose", level=2, comments=[])):
    print(_attr)
