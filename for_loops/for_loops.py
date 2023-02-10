for k in [1,2,3]:
    print(k)

for char in ["a", "b", "c"]:
    print(char)

for func in [max, min, abs]:
    print(func)

def square(x):
    return x * x

for val in [128, 256, 512]:
    print(f"{square(val):>10,d}")



