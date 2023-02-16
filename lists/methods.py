L = ["a", "b", "c", "a", "a", "b"]

# count
assert L.count("a") == 3
assert L.count("c") == 1
assert L.count("x") == 0

assert L.index("a") == 0
assert L.index("b") == 1

# specify the start
assert L.index("a", 1) == 3

# append
L = ["a", "1"]
L.append("2")
assert L == ["a", "1", "2"]

# extend
L = ["a", "1"]
s = ["b", "c"]
L.extend(s)
assert L == ["a", "1", "b", "c"]

# insert
L = ["a", "1"]
L.insert(0, "x")
L.insert(0, "y")
L.insert(2, "z")
assert L == ["y", "x", "z", "a", "1"]

# remove
L = ["a", "1", "2", "1"]
L.remove("1")
assert L == ["a", "2", "1"]

# pop
L = ["a", "1", "2", "1"]
p = L.pop(1)
assert p == "1"
assert L == ["a", "2", "1"]
p = L.pop()
assert p == "1"
assert L == ["a", "2"]

# reverse
L = ["a", "b", "c"]
L.reverse()
assert L == ["c", "b", "a"]

# sort
L = ["c", "b", "a"]
L.sort()
assert L == ["a", "b", "c"]

# don't do this
L = [1, 2]
x = L.append(3)
assert x is None
assert L == [1, 2, 3]

L = [1, 2]
y = L.extend([3, 4])
assert y is None
assert L == [1, 2, 3, 4]

