
name = "Jose"

if name == "Jose":
    print(f"hi, {name}")
elif name == "Juan":
    print(f"hi, {name}")
else:
    print("I do not know you")


# WHILE

i = 0
while i < 10:
    if i == 6:
        break # break early
    i += 1
    if i == 5:
        continue # continue to next iteration
    print (f"Hi number {i}!")


