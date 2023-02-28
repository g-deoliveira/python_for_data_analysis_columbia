x = ["x1", "x2", "x3", "x4", "x5"]

actual = []
for i in zip(x):
    actual.append(i)

expected = [
    ("x1", ),
    ("x2", ),
    ("x3", ),
    ("x4", ),
    ("x5", ),
]

assert expected == actual

assert expected == list(zip(x))