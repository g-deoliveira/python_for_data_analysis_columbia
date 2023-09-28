PI = 3.1415926

CF_CONSTANT = 32
CF_SCALAR = 1.8
FC_SCALAR = 5 / 9

def area_of_circle(radius):
    return PI * radius ** 2

def volume_of_sphere(radius):
    return 4 / 3 * PI * radius ** 3

def celcius_to_fahrenheit(x):
    return CF_CONSTANT + CF_SCALAR * x

def fahrenheit_to_celcius(x):
    return FC_SCALAR * (x - CF_CONSTANT)

assert area_of_circle(1) == PI
assert volume_of_sphere(1) == 4 / 3 * PI
assert celcius_to_fahrenheit(20) == 68.0
assert fahrenheit_to_celcius(68) == 20.0

PI = 1.0
assert PI == 1
