x = [100, 200, "x", "yz"]

assert x[1:3] == [200, "x"]
assert x[2:4] == ["x", "yz"]
assert x[1:2] == [200]

assert x[:2] == [100, 200]
assert x[:1] == [100]

assert x[2:] == ["x", "yz"]
assert x[3:] == ["yz"]

assert x[:] == [100, 200, "x", "yz"]

assert x[-3:-1] == [200, "x"]
assert x[-2:] == ["x", "yz"]
assert x[:-2] == [100, 200]

assert x[:100] == [100, 200, "x", "yz"]
assert x[2:100] == ["x", "yz"]

assert x[-100:2] == [100, 200]

assert x[0:3:2] == [100, "x"]
assert x[:3:2] == [100, "x"]
assert x[::2] == [100, "x"]

assert x[-1:-3:-1] == ["yz", "x"]
assert x[::-1] == ["yz", "x", 200, 100]