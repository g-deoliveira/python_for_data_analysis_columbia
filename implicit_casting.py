# x is an int
x = 1
assert isinstance(x, int)

# y is a float
y = 99.0
assert isinstance(y, float)

# Adding x and y returns a float.
# x is implicitly cast from an int
# to a float during the operation.
z = x + y
assert isinstance(z, float)
assert z == 100.0
assert isinstance(x, int)

b = True
# here the boolean variable b is
# implicitly type cast to int
assert b + 9 == 10