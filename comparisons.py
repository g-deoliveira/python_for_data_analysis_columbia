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


