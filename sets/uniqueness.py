x = ["abc"] * 10
assert x.count("abc") == 10
assert len(x) == 10

y = set(x)
assert y == {"abc"}
assert len(y) == 1

x = [
    1, 1, 1, 2, 2,
    2, 2, 2, 3, 3,
    3, 3, 3, 3, 3,
]
assert isinstance(x, list)
assert len(x) == 15
assert x.count(1) == 3
assert x.count(2) == 5
assert x.count(3) == 7

y = set(x)
assert len(y) == 3
