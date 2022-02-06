
# Empty print statement prints an empty line
print()

# You can print variables using the print function
print('Hello World.')

# you can pass unlimited number of arguments
# (of different types) to the print function
x = 123.0
y = False
z = 'wow'
print('hello', x, y, z, 'goodbye')


# If you want to print quotes, you simply surround
# single quotes by double quotes or vice-versa
print('And then he said, "Hello!!"')
print("Don't you worry,it's going to be okay.")

# alternatively you can the backslash escape character for
# single quotes (or double quotes):
print("And then he said, \"Hello!!\"")
print('Don\'t you worry,it\'s going to be okay.')

# this means if you try to print a backslash, you need to
# escape it
print('The single backslash here generates a SyntaxError: \')
print('This is going to work: \\') # the backslash is escaped

# the newline \n and tab \t characters:
print('Linebreak:\nNew line\ttab')
print('\t1')
print('\t2')

