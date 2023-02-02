def change_x(x):
    x = 100
    print("in change_x, x=", x)


x = 10
print("prior to change_x, x=", x)
change_x(x)
print("after the call to change_x, x=", x)


def change_and_return_x(x):
    x = 100
    print("in change_x, x=", x)
    return x

print("\nprior to change_and_return_x, x=", x)
x = change_and_return_x(x)
print("after the call to change_and_return_x, x=", x)


def change_a_mutable_object(x):
    x[0] = 0

x = [10, 20, 30]
print("\nprior to change_a_mutable_object, x=", x)
change_a_mutable_object(x)
print("after the call to change_a_mutable_object, x=", x)
