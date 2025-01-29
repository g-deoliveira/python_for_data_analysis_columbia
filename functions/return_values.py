def f():
    return None

def g():
    print("hello")

def h():
    pass

assert f() is None
assert g() is None
assert h() is None

def one():
    return "one"

assert one() == "one"

def one_and_two():
    return "one", "two"

assert one_and_two() == ("one", "two")
