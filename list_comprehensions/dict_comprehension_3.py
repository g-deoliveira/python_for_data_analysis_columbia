import string

N = 5

keys = string.ascii_lowercase[:N]
vals = range(N)
conditions = [1]*int(N/2) + [3]*int(N/2)
conditions += [5] * (N - len(conditions))
assert len(keys) == len(vals) == len(conditions)

d = {k:v for k,v in zip(keys,vals) if v > 0 and v < 3}
assert d == {"b":1, "c":2}

def f(u, suffix="_0"):
    return str(u) + suffix

def p(u, exp=1):
    return pow(u, exp)

d = {k:f(v) for k,v,c in zip(keys,vals, conditions) if v >= c}
assert d == {"b":"1_0", "d":"3_0"}

def c(u):
    return u if u % 2 == 0 else None

d = {f(k):p(v) for k,v in zip(keys,vals) if c(v)}
assert d == {"c_0":2, "e_0":4}
