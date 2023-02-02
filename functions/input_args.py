def positional_args(x, y, z):
    return x * y + z

assert positional_args(2, 4, 8) == 16
assert positional_args(4, 2, 8) == 16
assert positional_args(4, 8, 2) == 34


def keyword_args(x, y, z):
    return x * y + z

assert keyword_args(x=2, y=4, z=8) == 16
assert keyword_args(y=4, x=2, z=8) == 16
assert keyword_args(y=4, z=8, x=2) == 16
