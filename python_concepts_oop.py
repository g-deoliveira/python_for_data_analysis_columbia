# define an integer
x = 8

# since an integer is also an object,
# it has methods and attributes.

# Here are some methods of x
assert x.as_integer_ratio() == (8, 1)
assert x.bit_count() == 1

# Here are some attributes of x
assert x.denominator == 1
assert x.numerator == 8
