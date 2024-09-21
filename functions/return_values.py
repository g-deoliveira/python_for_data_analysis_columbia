def f():
    return None

def g():
    print("hello")

def h():
    pass

assert f() is None
assert g() is None
assert h() is None

def f(x, y):
    return (
        x,
        y,
        [x, y],
        {x:y}, (x, y),
        "".join([str(x),str(y)])
    )

assert f(1, 2) == (1, 2, [1, 2], {1: 2}, (1, 2), "12")
