

def display_hello():
    '''
    This function:
    - takes no input arguments
    - prints "hello 1" to the screen
    - returns None (implicitly)
    '''
    print('hello 1')

result = display_hello()
assert result is None


def display_hello2():
    '''
    This function:
    - takes no input arguments
    - prints "hello 2" to the screen
    - returns None (explicitly)
    '''
    print('hello 2')
    return None

result = display_hello2()
assert result is None


def display_text(text):
    '''
    This function:
    - takes 1 input argument: text
    - prints the input to the screen
    - returns None (implicitly)
    '''
    print(text)

value = 'This is a string!!'
result = display_text(value)
assert result is None


def display_text_n_times(text, n):
    '''
    This function:
    - takes 2 input arguments: text and n
    - prints the input to the screen, n times
    - returns None (implicitly)
    '''
    for k in range(n):
        print(text)

n = 3
value = 'This string is going to be repeated 3 times'
result = display_text_n_times(value, n)
assert result is None


def display_text_n_times_with_default(text, n=1):
    '''
    This function:
    - takes 2 input arguments: text and n
    - n has a default value of 1
    - prints the input to the screen, n times
    - returns None (implicitly)
    '''
    for k in range(n):
        print(text)

value = 'This string is NOT going to be repeated'
result = display_text_n_times_with_default(value)
assert result is None


def using_named_input_args(x=1, y=2, z=3):
    '''
    This example demonstrates how you can
    pass arguments to functions.
    It displays the input values
    and returns (x + y) * z
    '''
    print(f'x={x} y={y} z={z}')
    return (x + y) * z

# calling the function without inputs
assert using_named_input_args() == 9, 'Failure 1 here'

# here I am going to pass different values
assert using_named_input_args(3,2,1) == 5, 'Failure 2 here'

# here I am going to pass in named arguments but in different order
assert using_named_input_args(z=3, y=2, x=1) == 9, 'Failure 3 here'


# note when setting up default arguments for a function,
# those have to be defined after all non-default args are defined
#
# eg this is okay:
#
#   def example1(pet1, pet2, pet3='dog', pet4='cat'):
#       ...
#
# but this is not:
#
#   def example2(pet1='dog', pet2='cat', pet3, pet4):
#       ...
#


# Examples:

# notice that the built-in function sum can add the elements
# of a list together as long as they are numeric and defined
#
# eg:  sum( [1,2,3] ) returns 6
#      sum( [1,2,3,None]) returns an Exception
#
# lets built a function that sums integers in a list and
# handles None

def my_sum1(data):
    '''
    input:
        data: a list of integers (or Nones)

    output:
        the sum of the integers in x
    '''
    s = 0
    for item in data:
        if item is None:
            continue
        s += item
    return s

x = [1,2,3,4]
assert my_sum1(x) == 10, f'Error in my_sum1 for x={x}'

x = [1,2,3,4, None]
assert my_sum1(x) == 10, f'Error in my_sum1 for x={x}'
