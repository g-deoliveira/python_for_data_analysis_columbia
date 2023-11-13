
# this lambda function returns the variable:
lambda x: x

# it is equivalent to this function
def example1(x):
    return x

# this function admits a parameter `x` and a
# function `func` and returns `func(x)`
def my_function(x, func):
    return func(x)

# here we provide a default value for `func` so that
# my_function(x) just returns x if `func` is not
# specified
def my_function(x, func=lambda x: x):
    return func(x)

assert my_function("cat") == "cat"
assert my_function("cat", lambda x: x[-1]) == "t"
