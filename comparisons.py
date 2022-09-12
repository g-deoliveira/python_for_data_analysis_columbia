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

# string representation of an int is not equal to that int
# but more importantly this comparison does not generate an error
assert not ('123' == 123)

# on the other hand, uncomment and run this single line of code
#'123' < 123
# it generates a TypeError because '<' is not supported
# between instances of 'str' and 'int'

# take advantage of the short-circuit to avoid errors
x = '123'
isinstance(x, int) and x < 123 # isinstance() returns False
# so short-circuiting prevents the second comparison, which
# would generate the exception.