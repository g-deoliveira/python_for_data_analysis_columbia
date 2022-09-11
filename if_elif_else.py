x = 10

if x is None:
    print('x is None')
elif not isinstance(x, int):
    print('x is not an integer')
elif x < 0:
    print('x is negative')
elif x > 0:
    print('x is positive')
else:
    print('x is zero')

y = -8

if y is None:
    print('y is None')
elif not isinstance(y, int):
    print('y is not an integer')
else:
    # y is an integer
    if y < 0:
        print('y is negative')
        if y % 2 == 0:
            print('y is even')
        else:
            print('y is odd')
    elif y > 0:
        print('y is positive')
        if y % 2 == 0:
            print('y is even')
        else:
            print('y is odd')
    else:
        print('y is zero')


