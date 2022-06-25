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
