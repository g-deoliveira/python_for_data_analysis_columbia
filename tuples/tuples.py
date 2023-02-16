t = ("a", "b", "c", "a", "a", "b", )

# count
assert t.count("a") == 3
assert t.count("c") == 1
assert t.count("x") == 0

# index
assert t.index("a") == 0
assert t.index("b") == 1

# index: specify the start
assert t.index("a", 1) == 3

