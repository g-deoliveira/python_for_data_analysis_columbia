def sum_n_digits(n):
    s = 0
    for k in range(n):
        s += k
    return s

def exact_formula(n):
    return n * (n + 1) / 2

for k in range(101):
    sum_n = sum_n_digits(k+1)
    exact = exact_formula(k)
    assert sum_n == exact

    if k % 10 == 0:
        print(f"{k:3d}: {sum_n:6,d}")
