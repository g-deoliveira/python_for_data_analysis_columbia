N = 5

# for loop
numbers_1 = []
for k in range(N):
    numbers_1.append(k)

# convert range to list
numbers_2 = list(range(N))

# list-comprehension
numbers_3 = [k for k in range(N)]

# verification
assert (numbers_1
        == numbers_2
        == numbers_3
        == [0, 1, 2, 3, 4]
        )
