def clean_up(val):
    """
    val: string that stores a numeric value
    this function cleans up the val:
        clip to range 0 to 100
        and round to the nearest integer
    """
    # clip values
    val = float(val)
    if val < 0:
        val = 0
    if val > 100:
        val = 100

    # round - implicitly converts to int
    val = round(val)

    return val

def get_value(input_number):
    # the input_number is used to enumerate the instructions
    text = """
    {}: Enter an integer between 0 and 100.
    Note: Values outside the expected range are clipped.
            Values are rounded to the nearest integer."""
    print(text.format(input_number))

    return input("\t> ")

value_1 = get_value(1)
value_1 = clean_up(value_1)

# now collect value_2
value_2 = get_value(2)
value_2 = clean_up(value_2)

print(f"\nThe cleaned up values are {value_1} and {value_2}.\n")
