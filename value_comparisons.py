<<<<<<< HEAD
# define these variables
temperature = 82
is_raining = True

=======
# define some variables
temperature = 82
is_raining = True

# assign the results of comparisons to other variables
>>>>>>> updates
is_hot_day = temperature > 80
is_hot_and_raining = is_hot_day and is_raining

assert is_hot_day
assert is_hot_and_raining

# define some variables
x = 10
y = "cat"
z = -4

test_1 = x >= 10 and y == "cat" and z < 0
assert test_1

# you can use parentheses to isolate tests and
# make these comparisons more readable
test_2 = (x >= 10) and (y == "cat") and (z < 0)
assert test_1 == test_2

# you can also group together comparisons
# in parentheses
test_3 = ((x >= 10 and y == "cat" and z < 0)
            or (x <=10 and y == "bird"))
assert test_3


