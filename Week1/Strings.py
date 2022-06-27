import datetime
from typing import List

multi_line = '''This
is
a
multiline
string'''

string_length = len("my string")

my_string = "Hello World!"
first_char = my_string[0]
last_char = my_string[-1]
sub_string = my_string[2:5]
sub_string = my_string[:3]

# NOTE: ranges do not error if out of bounds

l_count = my_string.count("l")

# CONCAT

print("Hello " + "World")
print("Hello" * 3) # -> HelloHelloHello


# FORMAT

name = "Jose"
age = "30"
print('My name is {0}, and I\'m {1}'.format(name, age))
print(f'My name is {name}, and I\'m {age}') # format shorthand

## Format numbers and dates
formated_number: str = "{:,}".format(1000000000) # -> 1,000,000,000

my_date: datetime.datetime = datetime.datetime(2020, 7, 4, 12, 15, 58)
formatted_date = "{:%Y-%m-%d %H:%M:%S}".format(my_date) # -> '2020-07-04 12:15:58'

percentage = '{:.2%}'.format(190/220) # -> 86.36%


# Format table
width=8
print(' decimal      hex   binary')
print('-'*27)
for num in range(1,16):
    for base in 'dXb':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()


# JOIN
shopping_list: List[str] = ["bread", "milk", "eggs"]
shopping_list_string: str = ",".join(shopping_list) # -> "bread, milk, eggs"
