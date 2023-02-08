s = 0
for k in [1,2,3]:
    s += k

assert s == 3 * 4 / 2



s = 0
for k in [1,2,3,4]:
    s += k

assert s == 4 * 5 / 2

s = 0
for k in [1,2,3,4,5]:
    s += k

assert s == 5 * 6 / 2

s = 0
for k in range(5):
    s += k

assert s == 4 * 5 / 2

def sum_n_digits(n):
    s = 0
    for k in range(n):
        s += k
    return s

for k in range(100):
    if k % 10 != 0:
        continue
    sum_n = sum_n_digits(k+1)

    print(sum_n, k * (k+1)/2)
