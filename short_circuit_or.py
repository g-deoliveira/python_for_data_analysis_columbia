# suppose we want to assign `x` a
# default value if its value is 0
x = 0
default = 9999

y = x or default
assert y == 9999 # this passes

# suppose we want to assign `x` a
# default value if it's an empty list
x = []
default = [9999]

y = x or default
assert y == [9999] # this passes

# example where default is not
# utilized
x = 10
default = 9999

y = x or default
assert x == 10