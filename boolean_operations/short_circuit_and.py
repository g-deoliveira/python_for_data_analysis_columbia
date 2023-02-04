def comparison(a,b,c,d):

    val = (a < b) and (b < c) and (c < d)

    return val

x,y,z = 100, 5, 10
val = x and y and z
assert val == z

x,y,z = 0, 5, 10
val = x and y and z
assert val == x

x,y,z = 0, 0, 10
val = x and y and z
assert val == y

x,y = 0, "1"
val = False
if (isinstance(x, int)
    and isinstance(y, int)
    and x < y):
    val = True
assert not val
