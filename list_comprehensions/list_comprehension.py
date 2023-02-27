
# simple list comprehension
my_list = [0, 3, 5]
assert [3*x for x in my_list] == [0, 9, 15]

# another example using built-in pow function
assert [pow(2,x) for x in my_list] == [1, 8, 32]

# another example
floor, ceiling = 2, 4
assert [max(floor, min(x, ceiling)) for x in my_list] == [2, 3, 4]

# here is a list
animals = ['cat', 'dog', 'fish', 'bird']

# use a list-comprehension to pluralize each animal in the list
y = [animal + 's' for animal in animals]
assert y == ['cats', 'dogs', 'fishs', 'birds']

# the plural of fish is fishes, not "fishs"
# we'll fix this using a conditional expression

# conditional expressions (ternary operator)
condition = True
x = 1 if condition else 0
assert x == 1

condition = False
x = 1 if condition else 0
assert x == 0

# now back to the pluralizing the animals list
# define a dictionary that overrides the
# plural of an animal. If the animal is not
# in the dictionary, then the rule is simply add 's'
plural_override = {
    'fish': 'fishes'
}

# here is the updated list-comprehension
y = [plural_override.get(animal)
     if plural_override.get(animal)
     else animal + 's'
     for animal in animals
    ]
assert y == ['cats', 'dogs', 'fishes', 'birds']

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


