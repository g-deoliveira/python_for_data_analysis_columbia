x = [41, 3.1415, True, "hello world"]

assert x[0] == 41
assert x[1] == 3.1415
assert x[2] == True
assert x[3] == "hello world"

assert x[-1] == "hello world"
assert x[-2] == True
assert x[-3] == 3.1415
assert x[-4] == 41

x[0] = 1
x[1] = "cat"
x[2] = 0.1
x[3] = False

assert x == [1, "cat", 0.1, False]