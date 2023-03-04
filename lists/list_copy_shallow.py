

x = [["a", 1], ["b", 2], ["c", 3]]

y = list(x)

y[0] = 999
assert x == [["a", 1], ["b", 2], ["c", 3]]
assert y == [999, ["b", 2], ["c", 3]]

y[1][0] = "x"
y[1][1] = 999
assert x == [["a", 1], ["x", 999], ["c", 3]]
assert y == [999, ["x", 999], ["c", 3]]

assert id(x) != id(y)
assert id(x[1]) == id(y[1])
