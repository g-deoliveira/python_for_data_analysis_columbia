def flip(a, b):
    return b, a

assert flip(1, 2) == (2, 1)


c = flip(1, 2)
assert c == (2, 1)

a1, b1 = flip(1,2)
assert b1, a1 == (1, 2)