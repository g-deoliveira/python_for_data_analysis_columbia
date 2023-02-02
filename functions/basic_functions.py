
def do_nothing():
    pass

x = do_nothing()
assert x is None


def print_hello1():
    # print_hello1 returns None (implicitly)
    print('hello1')

result = print_hello1()
assert result is None


def print_hello2():
    # print_hello2 returns None (explicitly)
    print('hello2')
    return None

result = print_hello2()
assert result is None


def return_text(text):
    return text

value = 'some random text'
result = return_text(value)
assert result == value


def print_and_return_text(text):
    print(text)
    return text

value = 'more random text'
result = print_and_return_text(value)
assert result == value


def print_text_n_times(text, n):

    for k in range(n):
        print(text)
    return text, n

n = 3
value = 'This string is going to be repeated'
result = print_text_n_times(value, n)
assert result == (value, n)


def print_text_n_times_with_default(text, n=1):
    # n has a default value of 1
    for k in range(n):
        print(text)

value = 'This string is NOT going to be repeated'
result = print_text_n_times_with_default(value)
assert result is None


def using_named_input_args(x=1, y=2, z=3):

    print(f'x={x} y={y} z={z}')
    return (x + y) * z

# calling the function without inputs
assert using_named_input_args() == 9

# now the order of the input arguments is reversed
assert using_named_input_args(3,2,1) == 5

# pass the input arguments by name
assert using_named_input_args(z=3, y=2, x=1) == 9


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
