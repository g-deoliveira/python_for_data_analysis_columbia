


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


# convert numbers to strings:
x = 123.123
x = str(x)

# convert strings to numbers
x = '12'
y = '14'
z = int(x) + int(y)
z = str(z)

# convert integers to booleans
assert bool(1) is True
assert bool(0) is False