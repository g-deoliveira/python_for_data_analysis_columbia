x,y,a,b = 0,0,0,0

val = (x < y) and (a < b)

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

