x = set()

assert isinstance(x, set)
assert len(x) == 0
assert "x" not in x
assert 1 not in x

x = {1, 2, 3, "x", "y", "z"}

assert len(x) == 6
assert "x" in x
assert 1 in x

for k in x:
    print(k)

y = [3, 6, 9, "u", "v", "w"]
assert isinstance(y, list)
x = set(y)
assert isinstance(x, set)
x = list(x)
assert isinstance(x, list)

y = (3, 6, 9, "u", "v", "w")
assert isinstance(y, tuple)
x = set(y)
assert isinstance(x, set)
x = tuple(x)
assert isinstance(x, tuple)
