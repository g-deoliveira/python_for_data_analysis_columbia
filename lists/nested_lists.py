x = ["a", "b"]

# set the second element to a list
x[1] = ["b", "c"]

assert x == ["a", ["b", "c"]]
assert x[0] == "a"
assert x[1] == ["b", "c"]
assert x[1][0] == "b"
assert x[1][1] == "c"

x[0] = [1, 2]
assert x == [[1, 2], ["b", "c"]]
