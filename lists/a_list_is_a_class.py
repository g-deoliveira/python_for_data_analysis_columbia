# when you define a variable as a list, you
# instantiate an object of type list
x = list()
assert isinstance(x, list)

# this list is empty
assert len(x) == 0

# Lists in Python are defined as a class. This
# means they have methods and attributes.
# Methods are functions defined for the class,
# which means they can be called by any object
# of that class. Here we introduce the append
# method for lists, which takes an input argument
# and adds it to the end of the list.
x.append("cat")
# The append method took the input, `cat` and
# added it to the end of the list `x`:
assert x == ["cat"]
assert len(x) == 1

# we can call the method again to add
# another element to the list
x.append(100)
assert x == ["cat", 100]
assert len(x) == 2
