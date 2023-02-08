for k in [1,2,3]:
    print(k)

for k in ["a", "b", "c"]:
    print(k)

for k in [max, min, abs]:
    print(k)

def square(x):
    return x * x


for k in [128, 256, 512]:
    print(f"{square(k):>10,d}")



