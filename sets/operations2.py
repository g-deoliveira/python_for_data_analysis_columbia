x = {1, 2, 3}
y = {2, 3, 4, 5}

z = x.difference(y)
assert z == {1}
# alternative syntax
assert z == x - y

z = y.difference(x)
assert z == {4, 5}

z = x.symmetric_difference(y)
assert z == {1, 4, 5}
# alternative syntax
assert z == x ^ y
# commutative
assert x ^ y == y ^ x
