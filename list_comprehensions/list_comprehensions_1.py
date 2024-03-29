N = 6

# for loop
numbers_1 = []
for k in range(N):
    numbers_1.append(k)

# list-comprehension
numbers_2 = [k for k in range(N)]

# verification
assert (numbers_1
        == numbers_2
        == [0, 1, 2, 3, 4, 5]
        )
