x = [5, 10, 15, 20, 25]
y = [2,  4,  6,  8, 10]
z = ["a", "b", "c"]

actual = []
for i,j,k in zip(x, y, z):
    actual.append((i,j,k))

expected = [
    ( 5,  2, "a"),
    (10,  4, "b"),
    (15,  6, "c"),
]

assert expected == actual

assert expected == list(zip(x,y,z))