
# this lambda function returns the variable:
lambda x: x

# it is equivalent to this function
def example(x):
    return x

# example of an anonymous function:
items = [
    (80, 90),
    (10, 20),
]
items.sort(key=lambda x: x[1])
assert items == [(10, 20), (80, 90)]

# non-anonymous formulation:
def second_element(x):
    return x[1]
items.sort(key=second_element, reverse=True)
assert items == [(80, 90), (10, 20)]

# multi-variable lambda function:
f = lambda x,y: x + y
assert f(1, 2) == 3

# using conditional operator
f = lambda x: "even" if x % 2 == 0 else "odd"
assert f(2) == "even"
