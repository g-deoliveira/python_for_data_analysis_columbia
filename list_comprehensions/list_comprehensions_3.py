N = 6

# for loop
numbers_1 = []
for k in range(N):
    if k >= 3:
        numbers_1.append(pow(2, k))

# list-comprehension
numbers_2 = [pow(2, k) for k in range(N) if k >= 3]

# verification
assert (numbers_1
        == numbers_2
        == [8, 16, 32]
        )
