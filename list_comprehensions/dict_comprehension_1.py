import string

N = 3

d = {k:None for k in string.ascii_lowercase[:N]}
assert d == {"a":None, "b":None, "c":None}

d = {k:100 for k in string.ascii_lowercase[:N]}
assert d == {"a":100, "b":100, "c":100}

d = {k:k for k in string.ascii_lowercase[:N]}
assert d == {"a":"a", "b":"b", "c":"c"}

d = {k:k+"0" for k in string.ascii_lowercase[:N]}
assert d == {"a":"a0", "b":"b0", "c":"c0"}

d = {k+"0":k for k in string.ascii_lowercase[:N]}
assert d == {"a0":"a", "b0":"b", "c0":"c"}

def f(u, suffix="_0"):
    return u + suffix

def g(u, repeat=1):
    return u * repeat

d = {f(k):g(k,2) for k in string.ascii_lowercase[:N]}
assert d == {"a_0":"aa", "b_0":"bb", "c_0":"cc"}
