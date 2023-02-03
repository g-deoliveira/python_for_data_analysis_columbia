x,y,z = 0, 5, 10
val = x < y or y < z
assert val

x,y,z = 10,5,3
val = x < y or y < z
assert not val

x,y,z = 100, 5, 10
val = x or y or z
assert val == x

x,y,z = 0, 5, 10
val = x or y or z
assert val == y

x,y,z = 0, 0, 10
val = x or y or z
assert val == z

x,y,z = 0, 0, ""
val = x or y or z
assert val == z

def black_box():
    return None

default = 9999
y = black_box() or default
assert y == 9999
