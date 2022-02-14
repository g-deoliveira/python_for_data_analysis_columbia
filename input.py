
# the input function without a prompt
x = input()
assert isinstance(x, str)

# here the expected type is a number
x = input('Enter a number between 1 and 9:\n')

while not (x.isnumeric() and int(x) >= 1 and int(x) <= 9):
    x = input('Enter a number between 1 and 9:\n')

print('The number is:', x)