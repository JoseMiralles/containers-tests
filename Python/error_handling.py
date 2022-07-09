
a = 12

try:
    print(len(a))
except:
    print("An error occured!")


# Handle specific errors
a = 100
b = 0

try:
    answer = a / b
except ZeroDivisionError:
    answer = None    # there's no answer
except:
    pass # do nothing

print (answer)


# ELSE and Finally statment

file = "file.txt"

try:
    f = open(file, "r")
except:
    print ("ERROR")
else:
    print(file, "opened successfully")
    f.close()
finally:
    pass # Do stuff here

