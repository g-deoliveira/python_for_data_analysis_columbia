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

