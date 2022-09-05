# The print function is a built-in Python function
# that displays the input to the "text stream"
print('Hello World.')

# You can pass an unlimited number of comma-separated
# arguments (of different types) to the print function
x = 123.0
y = False
z = 'wow'
print('hello', x, y, z, +1, -2, 'goodbye')

# Empty print statement prints an empty line
print()

# If you want to print quotes, you simply surround
# single quotes by double quotes or vice-versa
print('And then he said, "No soup for you!!"')
print("Don't worry, it's going to be okay.")

# alternatively you can the backslash escape character for
# single quotes (or double quotes):
print("And then he said, \"Hello!!\"")
print('Don\'t you worry,it\'s going to be okay.')

# this prints a single quote
print('\'')

# this means if you try to print a backslash, you need to
# escape it
print('The single backslash here generates a SyntaxError: \')
print('This is going to work: \\') # the backslash is escaped

# the newline \n and tab \t characters:
print('Linebreak:\nNew line\ttab')
print('\t1')
print('\t2')

