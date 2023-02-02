def my_operation(x, y):

    def my_product(a, b):
        return a * b

    product = my_product(x, y)
    return product

assert my_operation(2, -3) == -6


def my_pythonic_operation(x, y):

    def my_product(a, b):
        return a * b

    return my_product(x, y)

assert my_pythonic_operation(2, -3) == -6