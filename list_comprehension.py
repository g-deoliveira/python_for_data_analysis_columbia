
# here is a list
animals = ['cat', 'dog', 'fish', 'bird']

# use a list-comprehension to append
# an 's' to each element in x
y = [animal + 's' for animal in animals]

assert y == ['cats', 'dogs', 'fishs', 'birds']

# another example:
assert [3*x for x in range(3)] == [0, 3, 6]

# add logic to the list-comprehension
# use a conditional expression in a list comprehension
is_land_animal = {
    'dog': True,
    'cat': True,
    'bird': False,
    'fish': False,
}
y = [animal for animal in animals if is_land_animal[animal]]

assert y == ['cat', 'dog']

# conditional expressions (ternary operator)
condition = True
x = 1 if condition else 0
assert x == 1

condition = False
x = 1 if condition else 0
assert x == 0


