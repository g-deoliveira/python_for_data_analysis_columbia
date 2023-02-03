# val is equal to x < y
# and y < z is not evaluated
x,y,z = 0, 5, 10
val = x < y or y < z
assert val

# val is equal to y < z
x,y,z = 10,5,3
val = x < y or y < z
assert not val

# val takes on the value of the
# first truth that is encountered
x,y,z = 100, 5, 10
val = x or y or z
assert val == x

# val takes on the value of the
# first truth that is encountered
x,y,z = 0, 5, 10
val = x or y or z
assert val == y

# val takes on the value of the
# first truth that is encountered
x,y,z = 0, 0, 10
val = x or y or z
assert val == z

# here val takes on the value of the
# last value
x,y,z = 0, 0, ""
val = x or y or z
assert val == z

# suppose we want to assign `x` a
# default value if its value is 0
# (or None, empty list, ...)
x = 0
default = 9999

y = x or default
assert y == 9999
