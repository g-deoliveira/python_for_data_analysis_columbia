
D = {"x":1, "y":2, "z": 3}

# D.items()
assert list(D.items()) == [('x', 1), ('y', 2), ('z', 3)]

for k, v in D.items():
    print(f"k={k}  v={v}")


# D.keys()
assert list(D.keys()) == ["x", "y", "z"]
# this is similar to list(D)
assert list(D) == list(D.keys())

for k in D.keys():
    print(k)

# D.values()
assert list(D.values()) == [1, 2, 3]
for v in D.values():
    print(v)
