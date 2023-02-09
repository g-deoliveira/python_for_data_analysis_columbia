x = [1, 2, 3]
y = x
y[0] = -1
assert x == [-1, 2, 3]
assert y == [-1, 2, 3]
assert id(x) == id(y)

y = x[:]
y[0] = 10
assert x == [-1, 2, 3]
assert y == [10, 2, 3]
assert id(y) != id(x)

y = x.copy()
assert x == [-1, 2, 3]
assert y == [-1, 2, 3]
assert id(y) != id(x)
