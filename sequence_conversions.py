# instantiate a tuple
t = 1,2,3
assert isinstance(t, tuple)

# convert the tuple to a list
m = list(t)
assert isinstance(m, list)
assert m == [1, 2, 3]

# convert the list back to a tuple
y = tuple(m)
assert isinstance(y, tuple)
assert y == (1, 2, 3)
assert t == y

# multiple conversions for demonstration
assert list(tuple(list(t))) == [1, 2, 3]
assert tuple(list(tuple(t))) == (1, 2, 3)

text = "cats"
assert list(text) == ["c", "a", "t", "s"]
assert tuple(text) == ("c", "a", "t", "s")


D = {"x": 1, "y": 20}
assert list(D) == ["x", "y"]
assert tuple(D) == ("x", "y")

for key in list(D):
    print(key, D[key])

