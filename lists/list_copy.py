x = [1, 2, 3]
y = x
assert id(x) == id(y)

y[0] = 999
assert x == [999, 2, 3]
assert y == [999, 2, 3]

x = [1,2,3]
y = list(x)
assert id(y) != id(x)

y[0] = 999
assert x == [1, 2, 3]
assert y == [999, 2, 3]

# shallow copies
y = x[:]
y = x.copy()
