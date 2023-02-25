x = set()

x.add(1)
assert x == {1}
len(x) == 1

x.add(2)
assert x == {1, 2}
assert x == {2, 1}
len(x) == 2

x.add("a")
x.add("a")
x.add("a")
assert x == {1, 2, "a"}
assert len(x) == 3

y = {1, 1, 1, 2, 3}
x.update(y)
assert x == {1, 2, "a", 3}
assert len(x) == 4

z = x.pop()
assert z in {1, 2, "a", 3}
assert len(x) == 3

z = x.pop()
z = x.pop()
z = x.pop()
assert len(x) == 0
