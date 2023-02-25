x = {1, 2, 3}
y = {2, 3, 4, 5}

z = x.intersection(y)
assert z == {2, 3}
assert z == {3, 2}
# alternative syntax
assert z == x & y
# commutative
assert x & y == y & x

z = x.union(y)
assert z == {2, 3, 5, 4, 1}
# alternative syntax
assert z == x | y
# commutative
assert x | y == y | x

