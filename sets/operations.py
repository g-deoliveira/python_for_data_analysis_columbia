
x = {1, 2, 3}
y = {2, 3, 4, 5}


z = x.intersection(y)
assert z == {2, 3}
assert z == {3, 2}
assert z == x & y       # syntax
assert x & y == y & x   # commutative


z = x.union(y)
assert z == {2, 3, 5, 4, 1}
assert z == x | y      # syntax
assert x | y == y | x  # commutative


z = x.difference(y)
assert z == {1}
assert z == x - y        # syntax


z = x.symmetric_difference(y)
assert z == {1, 4, 5}
assert z == x ^ y        # syntax
assert x ^ y == y ^ x    # commutative
