def comparison(a,b,c):

    val = a and b and c

    return val

x,y,z = 100, 5, 10
val = x and y and z
assert val == z

x,y,z = 0, 5, 10
val = x and y and z
assert val == x

x,y,z = 5, 0, 10
val = x and y and z
assert val == y

x,y = 0, "1"
val = False
if (isinstance(x, int)
    and isinstance(y, int)
    and x < y):
    val = True
assert not val
