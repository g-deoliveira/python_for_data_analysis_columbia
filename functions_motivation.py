instructions = """
Instructions:
Enter {order} integer between 0 and 100.
Note: Values outside the expected range are clipped.
      Float values are rounded to the nearest integer."""

print(instructions.format(order="a first"))
value_1 = input(": ")

# clip values
value_1 = float(value_1)
if value_1 < 0:
    value_1 = 0
if value_1 > 100:
    value_1 = 100

# round if float (implicity converts to int)
# otherwise convert to int
if isinstance(value_1, float):
    value_1 = round(value_1)
else:
    value_1 = int(value_1)

# now collect value_2
print(instructions.format(order="a second"))
value_2 = input(": ")

# clip values
value_2 = float(value_2)
if value_2 < 0:
    value_2 = 0
if value_2 > 100:
    value_2 = 100

# round if is float
if isinstance(value_2, float):
    value_2 = round(value_2)
else:
    value_2 = int(value_2)

print(f"The inputted values are {value_1} and {value_2}.")
