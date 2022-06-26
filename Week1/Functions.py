
def sayHello():
    print("Hello!")

def average (num1, num2):
    return (num1/num2)

def sayHelloToPerson(name = "Nameless"):
    print(f"Hello {name}!")


# Using parameter keywords on invocation
sayHelloToPerson(name="Jose")


# Anonymous Functions
toUpper = lambda s: s.upper()

# Can be spread across multiple lines
toUpper = (
    lambda s:
        s.upper())