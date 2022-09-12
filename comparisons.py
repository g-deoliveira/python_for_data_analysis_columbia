assert 99 < 100
assert 100 <= 100

assert 100 > 99
assert 100 >= 100

assert 100 == 100
assert 99 != 100

x = None
y = 100
assert x is None
assert y is not None

# chained comparisons
assert 0 < 1 <= 1
# are equivalent to a sequence of comparisons
assert 0 < 1 and 1 <= 1

# comparing strings
x = "Orange"
y = "Orange"

assert x == y

# highlighting lexicographical order
x = "green"
y = "Green"

assert y < x # because unicode(G) < unicode(g)

# highlighting lexicographical order
x = "dog"
y = "doG"
assert y < x

# highlighting lexicographical order
x = "dogs"
y = "dog"
assert y < x

# you can check objects of different type for equality
assert '1' != 1     # comparing string to integer
assert 'g' != True  # comparing string to Boolean

assert not '123' == 123

# this code generates a TypeError
# TypeError: '<' not supported between instances of 'str' and 'int'
# uncomment to see the error:
#'123' < 123

# take advantage of the short-circuit to avoid errors
x = '123'
isinstance(x, int) and x < 123 # isinstance() returns False
# so short-circuiting prevents the second comparison, which
# would generate the exception.