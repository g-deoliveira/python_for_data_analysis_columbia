x = ["x1", "x2", "x3", "x4", "x5"]
y = [2,  4,  6,  8, 10]

actual = {}
for i,j in zip(x, y):
    actual[i] = j

expected = {
    "x1": 2,
    "x2": 4,
    "x3": 6,
    "x4": 8,
    "x5": 10,
}

assert expected == actual

assert expected == dict(zip(x,y))

actual = {}
n = len(x)
for k in range(n):
    actual[x[k]] = y[k]

assert expected == actual
