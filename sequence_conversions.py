t = 1,2,3
assert isinstance(t, tuple)

m = list(t)
assert isinstance(m, list)

y = tuple(m)
assert isinstance(y, tuple)

assert t == y


text = "cats"
assert list(text) == ["c", "a", "t", "s"]
assert tuple(text) == ("c", "a", "t", "s")
