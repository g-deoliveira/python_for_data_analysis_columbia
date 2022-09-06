# checking if an object is equal to none

x = None
assert x is None

x = 1
assert x is not None

# another case where short-circuiting
# allows you to handle cases where
# you want to avoid accidentally comparing
# a null variable to an integer
x = 5
y = x is not None and x < 10 # y is True

x = None
y = x is not None and x < 10 # y is False

x = None
y = x < 10 # generates a TypeError exception