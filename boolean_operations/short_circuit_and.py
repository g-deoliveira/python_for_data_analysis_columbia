# val is equal to y < z
# since x < y is True
x,y,z = 0, 5, 10
val = x < y and y < z
assert val == y < z

# val is equal to x < y since
# it's the first False encountered
x,y,z = 10,5,3
val = x < y and y < z
assert val == x < y

# val takes on the value of the
# last truth that is encountered
x,y,z = 100, 5, 10
val = x and y and z
assert val == z

# val takes on the value of the
# first False that is encountered
x,y,z = 0, 5, 10
val = x and y and z
assert val == x

# val takes on the value of the
# last value
x,y,z = 0, 0, 10
val = x and y and z
assert val == y

# here val takes on the value of the
# last value
x,y,z = 0, 0, [] # empty list
val = x or y or z
assert val == z

