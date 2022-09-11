# define these variables
temperature = 82
is_raining = True

is_hot_day = temperature > 80
is_hot_and_raining = is_hot_day and is_raining

assert is_hot_day
assert is_hot_and_raining

x = 10
y = "cat"
z = -4

test_1 = x >= 10 and y == "cat" and z < 0
assert test_1

# you can use parentheses to isolate tests and
# make these comparisons more readable
test_2 = (x >= 10) and (y == "cat") and (z < 0)
assert test_1 == test_2

test_3 = x > 20 or y == "bat" or z < 0
assert test_3


