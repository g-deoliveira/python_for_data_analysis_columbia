N = 6

# for loop
numbers_1 = []
for i,j in zip(range(N), range(N,0,-1)):
    numbers_1.append(i + j)

# list-comprehension
numbers_2 = [i + j for i,j in zip(range(N), range(N,0,-1))]

# alternatively
numbers_2 = [
    i + j
    for i,j
    in zip(range(N), range(N,0,-1))]

# verification
assert (numbers_1
        == numbers_2
        == [6, 6, 6, 6, 6, 6]
        )

def get_tuple(N):
    return zip(range(N), range(N,0,-1))

def my_sum(a, b):
    return a + b

numbers_2 = [my_sum(i,j) for i,j in get_tuple(N)]
assert numbers_2 == [6, 6, 6, 6, 6, 6]
