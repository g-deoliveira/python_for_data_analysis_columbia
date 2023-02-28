N = 6

# for loop
numbers_1 = []
for k in range(N):
    numbers_1.append(pow(2, k))

# list-comprehension
numbers_2 = [pow(2, k) for k in range(N)]

# verification
assert (numbers_1
        == numbers_2
        == [1, 2, 4, 8, 16, 32]
        )
