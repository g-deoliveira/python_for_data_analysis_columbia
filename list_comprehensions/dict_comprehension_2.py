import string

N = 3

keys = string.ascii_lowercase[:N]
vals = range(N)

d = {k:v for k,v in zip(keys,vals)}
assert d == {"a":0, "b":1, "c":2}

d = {v:k for k,v in zip(keys,vals)}
assert d == {0:"a", 1:"b", 2:"c"}

def f(u, suffix="_0"):
    return str(u) + suffix

def p(u, exp=1):
    return pow(u, exp)

d = {k:f(v) for k,v in zip(keys,vals)}
assert d == {"a":"0_0", "b":"1_0", "c":"2_0"}

d = {f(k):p(v) for k,v in zip(keys,vals)}
assert d == {"a_0":0, "b_0":1, "c_0":2}

d = {f(k):p(v, 3) for k,v in zip(keys,vals)}
assert d == {"a_0":0, "b_0":1, "c_0":8}
