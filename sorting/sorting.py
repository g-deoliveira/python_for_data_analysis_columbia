# sort a numerical list
x = [9, 8, 0, 4, -2]
assert sorted(x) == [-2, 0, 4, 8, 9]
# reverse the sort order
assert sorted(x, reverse=True) == [9, 8, 4, 0, -2]

# sort a string
x = "cat-attack"
assert (
    sorted(x)
    == ["-", "a", "a", "a", "c", "c", "k", "t", "t", "t"]
)
# reverse the sort order
assert (
    sorted(x, reverse=True)
    == ["t", "t", "t", "k", "c", "c", "a", "a", "a", "-"]
)

# sort a list of tuples
x = [(9, "z"), (8, "c"), (1, "e"), (-4, "a")]
assert sorted(x) == [ (-4, "a"), (1, "e"), (8, "c"), (9, "z")]
# reverse the sort order
assert (
    sorted(x, reverse=True)
    == [(9, "z"), (8, "c"), (1, "e"), (-4, "a")]
)

# specify the sort key
assert (
    sorted(x, key=lambda k: k[1])
    == [(-4, "a"), (8, "c"), (1, "e"), (9, "z")]
)
