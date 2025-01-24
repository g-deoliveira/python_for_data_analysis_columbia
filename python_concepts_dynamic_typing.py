# define a python function
# notice that types aren't specified
def sqr(x):
    return x * x

# you can pass in an integer
assert sqr(2) == 4

# you can pass in a float!
assert sqr(1.2) == 1.44

# Python DOES provide the ability to
# specify the types, however these are
# not enforced. They are used for
# informational purposes.
def sqr_with_type_hints(x: int) -> int:
    return x * x

# here the input is an integer
assert sqr_with_type_hints(2) == 4

# and here the input is a float!
assert sqr_with_type_hints(1.2) == 1.44
