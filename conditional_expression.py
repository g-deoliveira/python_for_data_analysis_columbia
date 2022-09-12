# Example 1
temperature = 50

wear_a_jacket = temperature < 40
# equivalent definition using conditional expression
wear_a_jacket = True if temperature < 40 else False


# Example 2
modify_scale_factor = True

if modify_scale_factor:
    scale_factor = 1.2
else:
    scale_factor = 1.0

# Example 2 is equivalent to:
scale_factor = 1.2 if modify_scale_factor else 1.0

# note that we replaced 4 lines of code with
# a single elegant and easy to read line.
