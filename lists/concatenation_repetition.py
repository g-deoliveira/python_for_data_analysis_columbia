x = [10, 20]
y = [30, 40]

z = x + y
assert z == [10, 20, 30, 40]

z = y + x
assert z == [30, 40, 10, 20]

assert x + [30] == [10, 20, 30]

assert [1] * 2 == [1, 1]
assert 2 * [1] == [1, 1]

assert ["a", "b"] * 2 == ["a", "b", "a", "b"]
assert 2 * ["a", "b"] == ["a", "b", "a", "b"]

