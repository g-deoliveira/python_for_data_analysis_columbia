x,y,z = 0, 5, 10
val = x < y and y < z
assert val == y < z

x,y,z = 10,5,3
val = x < y and y < z
assert val == x < y

x,y,z = 100, 5, 10
val = x and y and z
assert val == z

x,y,z = 0, 5, 10
val = x and y and z
assert val == x

x,y,z = 0, 0, 10
val = x and y and z
assert val == y

x,y,z = 0, 0, [] # empty list
val = x or y or z
assert val == z

