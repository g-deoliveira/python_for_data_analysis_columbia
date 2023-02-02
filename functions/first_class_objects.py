def my_sum(a, b):
    return a + b

add = my_sum
assert add(1,2) == 3

def my_operation(a, b, func):
    return func(a,b)

assert my_operation(1, 2, my_sum) == 3

def return_x(x):
    return x

def get_max_min(what):
    if what == "min":
        return min
    elif what == "max":
        return max
    else:
        return return_x


f = get_max_min("max")
assert f([1,2,3]) == 3

f = get_max_min("min")
assert f([1,2,3]) == 1

f = get_max_min("")
assert f([1,2,3]) == [1,2,3]