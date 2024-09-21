def add_10(x):
    y = x + 10
    return y

assert add_10(-10) == 0

def add_10_pythonic(x):
    return x + 10

assert add_10_pythonic(-10) == 0

def add(x, y):
    return x + y

assert add(1, 2) == 3

def my_max(x, y, z):
    max_xy = max(x, y)
    return max(max_xy, z)

assert my_max(1, 2, 3) == 3
assert my_max(3, 2, 1) == 3
assert my_max(1, 3, 2) == 3

def my_max(x, y, z):
    # could just use the build-in max function!
    return max(x, y, z)
