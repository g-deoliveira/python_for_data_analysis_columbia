def sum_n_digits(n):
    s = 0
    for k in range(n):
        s += k
    return s

for k in range(101):
    sum_n = sum_n_digits(k+1)
    exact = k * (k + 1) / 2
    assert sum_n == exact

    if k % 10 == 0:
        print(f"{k:3d}: {sum_n:6,d}")
