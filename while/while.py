print("before loop 1")
x = 0
while x > 1:
    print("in while loop 1")
print("after loop 1")


print("\nbefore loop 2")
x = 0
while x < 3:
    print(f"in while loop 2 with x={x}")
    x = x + 1
print(f"after loop 2 with x = {x}")


print("\nbefore loop 3")
x = 0
while x < 3:
    print(f"in while loop 3 with x={x}")
    x = x + 1
    if x > 1:
        print("break")
        break
print(f"after loop 3 with x = {x}")


print("\nbefore loop 4")
x = 0
while x < 3:
    print(f"in while loop 3 with x={x}")
    x = x + 1
    if x > 1:
        print("break")
        break
print(f"after loop 3 with x = {x}")
