N = 6

items = [1]*3 + [2]*3 + [3]*3

s = set()
for k in items:
    s.add(k)
assert s == {2, 1, 3}

s = {k for k in items}
assert s == {1, 2, 3}

s = {k for k in items if k != 2}
assert s == {3, 1}

s = {pow(2,k) for k in items if k > 1}
assert s == {4, 8}

