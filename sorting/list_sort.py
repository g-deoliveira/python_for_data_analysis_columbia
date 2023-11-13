# sort a numerical list using the built-in list sort method
x = [9, 8, 0, 4, -2]

x.sort()
assert x == [-2, 0, 4, 8, 9]

# reverse the sort order
x.sort(reverse=True)
assert x == [9, 8, 4, 0, -2]

# sort a list of tuples
x = [(9, "z"), (8, "c"), (1, "e"), (-4, "a")]
x.sort()
assert x == [ (-4, "a"), (1, "e"), (8, "c"), (9, "z")]

# reverse the sort order
x.sort(reverse=True)
assert x == [(9, "z"), (8, "c"), (1, "e"), (-4, "a")]

# specify the sort key
x.sort(key=lambda k: k[1])
assert x == [(-4, "a"), (8, "c"), (1, "e"), (9, "z")]
