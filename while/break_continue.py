x = 256
while x > 1:
    x /= 2
    print(f"x = {x}")
    if x < 10:
        break
print(f"The finl value of x is {x}.\n")

x = 0
while x < 6:
    x += 1
    if x % 2 == 1:
        continue
    print(f"even number x = {x}")
