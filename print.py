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

# You can the escape single and double quotes
print("The name of the song is \"Don't worry, be happy!!\"")

# this prints a single quote
print('\'')

# the newline \n and tab \t characters:
print('Linebreak:\nNew line\ttab')
print('\t1\t2\t3')
print('\t2')

## intro slide

how_complicated = 'quite'
qualifier = 'a few'
thing = 'thing'
action = 'we\'ll split printing out over several lectures.'

# example of f-string, released in Python 3.6
print(f"Printing in Python can get {how_complicated} complicated.")

# example of str.format, introduced in Python 2.6
text = "There are {q} different ways of accomplishing\nthe same {o}."
print(text.format(q=qualifier, o=thing))

# the original way of formatting, using %-formatting, now discouraged
print("As a result, %s" % action)
print("""
Otherwise, we, could, easily, spend an entire lecture on printing.
And nobody wants to sit through that!""")
print()



