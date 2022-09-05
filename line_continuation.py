a_variable_name = 1
a_long_variable_name = 2
a_longer_variable_name = 3
a_super_long_variable_name_123456890 = 4

# this is a long line: it is over 100 characters long
x1 = a_variable_name + a_long_variable_name + a_longer_variable_name + a_super_long_variable_name_123456890

# same line wrapped over several lines
x2 = a_variable_name \
    + a_long_variable_name + \
    a_longer_variable_name \
    + a_super_long_variable_name_123456890

assert x1 == x2
