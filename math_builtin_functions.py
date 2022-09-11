# absolute value
assert 10 == abs(10)
assert 10 == abs(-10)

# pow function
assert 32 == pow(2,5)
assert 0.25 == pow(2, -2)
assert 2 == pow(4, 0.5)

# round function
assert 3 == round(3.4)
assert 4 == round(3.6)

# iterables
x = [10, 4, -6]
assert max(x) == 10
assert min(x) == -6
assert sum(x) == 8
