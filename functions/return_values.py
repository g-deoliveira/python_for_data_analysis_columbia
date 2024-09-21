def f():
    return None

def g():
    print("hello")

def h():
    pass

assert f() is None
assert g() is None
assert h() is None

def func():
    return "one"

def f():
    return (
        1,
        2,
        [1, 2],
        {1:2}, (1, 2),
    )

assert f() == (1, 2, [1, 2], {1: 2}, (1, 2))
