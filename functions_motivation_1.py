print("""
1: Enter an integer between 0 and 100.
   Note: Values outside the expected range are clipped.
         Values are rounded to the nearest integer.""")

value_1 = input("> ")

# clip values
value_1 = float(value_1)
if value_1 < 0:
    value_1 = 0
if value_1 > 100:
    value_1 = 100

# round - implicitly converts to int
value_1 = round(value_1)

# now collect value_2
print("""
2: Enter an integer between 0 and 100.
   Note: Values outside the expected range are clipped.
         Values are rounded to the nearest integer.""")

value_2 = input("> ")

# clip values
value_2 = float(value_2)
if value_2 < 0:
    value_2 = 0
if value_2 > 100:
    value_2 = 100

# round - implicitly converts to int
value_2 = round(value_2)

print(f"\nThe cleaned up values are {value_1} and {value_2}.\n")
