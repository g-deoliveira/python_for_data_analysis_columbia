def positional_args(x, y, z):
    return x / y + z

assert positional_args(4, 2, 5) == 7
assert positional_args(2, 4, 5) == 5.5
assert positional_args(4, 5, 2) == 2.8


def keyword_args(x, y, z):
    return x / y + z

assert keyword_args(x=4, y=2, z=5) == 7
assert keyword_args(y=2, x=4, z=5) == 7
assert keyword_args(y=2, z=5, x=4) == 7


assert keyword_args(2, 4, z=5) == 5.5
assert keyword_args(2, y=4, z=5) == 5.5
assert keyword_args(2, z=5, y=4) == 5.5

def default_args(x=1, y=1, z=0):
    return x / y + z

assert default_args() == 1
assert default_args(z=2) == 3
assert default_args(y=2) == 0.5
assert default_args(z=2, y=2, x=2) == 3
assert default_args(2, 2, 2) == 3

def some_default_args(x, y=1, z=0):
    return x / y + z

assert some_default_args(0) == 0
assert some_default_args(3) == 3

