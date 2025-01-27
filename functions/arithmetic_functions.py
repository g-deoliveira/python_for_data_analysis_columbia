def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

assert add(1, 2) == 3
assert subtract(1, 2) == -1

output = add(1, 2) + subtract(1, 2)

assert output == 2
