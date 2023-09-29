# define a global variable
count = 0

# define a function that has a local variable named count
def the_count():
    count = 2
    return count

# define a function that refers to the global variable
def global_count():
    print(count)

# define a function that attempts to change the global variable
def change_global():
    print(count)
    count = count + 1

# define a function that defines a local variable and changes it
def change_local():
    count = 2
    count = count + 1
    return count

# assert statements
assert count == 0
assert the_count() == 2
assert global_count() is None

# this try-catch statement verifies that running change_global
# generates an error
try:
    change_global()
except UnboundLocalError:
    print("handled UnboundLocalError")

assert change_local() == 3

# if we declare the variable as global within the scope of
# the function, then we are telling the program we can
# access it and modify it from anywhere

# define a function that attempts to change the global variable
def change_global_new():
    global count
    print(count)
    count = count + 10
    return count

assert change_global_new() == 10
assert count == 10