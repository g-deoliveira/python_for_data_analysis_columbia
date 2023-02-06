x = 0
while x > 1:
    print("in while loop 1")


x = 0
while x < 3:
    print(f"in while loop 2 with x={x}")
    x = x + 1


x = 0
while x < 3:
    print(f"in while loop 3 with x={x}")
    x = x + 1
    if x > 1:
        break


x = 0
while True:
    print(f"in while loop 3 with x={x}")
    x = x + 1
    if x > 1:
        break
