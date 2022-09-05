


i = 80   # this is an integer
assert isinstance(i, int)
assert type(i) == int

x = 80.0  # this is a float
assert isinstance(x, float)
assert type(x) == float

c = 'cat'   # this is a string
assert isinstance(c, str)
assert type(c) == str

flag = True  # this is a boolean variable
assert isinstance(flag, bool)
assert type(flag) == bool

y = b'oo'    # this is a byte array
assert isinstance(y, bytes)
assert type(y) == bytes


# type cast numbers to strings:
x = 123.123
x = str(x)
assert isinstance(x, str)

# type cast strings to numbers
x = '12'
y = '14'
z = int(x) + int(y)
z = str(z)
assert isinstance(z, str)

# type cast integers to booleans
assert bool(1) is True
assert bool(0) is False

# this type cast will generate a ValueError
# because you can't represent 'abc' as a number
x = 'abc'
y = int(x)
