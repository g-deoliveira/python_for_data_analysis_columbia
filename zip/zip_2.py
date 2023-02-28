x = [5, 10, 15, 20, 25]
y = [2,  4,  6,  8, 10]

actual = []
for i, j in zip(x, y):
    actual.append((i, j))

expected = [
    ( 5,  2),
    (10,  4),
    (15,  6),
    (20,  8),
    (25, 10),
]

assert expected == actual

assert expected == list(zip(x,y))
