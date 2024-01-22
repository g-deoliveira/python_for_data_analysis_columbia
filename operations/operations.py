# power operator for exponentiation
assert 100 == 10 ** 2
assert 10 == 100 ** 0.5 # fractional exponents
assert 0.1 == 10 ** -1 # negative exponents

# note you can use the built-in operator `pow`
assert pow(2, 3) == 8

# multiplication
assert 30 == 10 * 3

# division
assert 2.25 == 9 / 4

# note, division returns a float
x = 10 / 2
assert isinstance(x, float)

# floor division
assert 2 == 9 // 4 # returns an int

# addition
assert 10 + 3 == 13

# subtraction
assert 10 - 3 == 7

# modulus
assert 11 % 4 == 3
