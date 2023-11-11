def divide(x, y):

    return x / y

assert divide(2, 1) == 2
assert divide(1, 2) == 0.5

# if you uncomment the next line,
# a ZeroDivisionError is generated:
# divide(1, 0)

# Handle the error using the try-except clause:
try:
    z = divide(1, 0)
except ZeroDivisionError as err:
    print(type(err), err)

# Example of ValueError:
try:
    x = int("abc")
except ValueError as err:
    print(type(err), err)

# Another example of ValueError
try:
    a, b = (1, 2, 3)
except ValueError as err:
    print(type(err), err)

# catch several errors:
try:
    ...
except ValueError as err:
    ...
except TypeError as err:
    ...
except Exception as err:
    ...

