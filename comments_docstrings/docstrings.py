
def one_line_docstring(text):
    """This function has a one-line docstring."""

    return text


def complex(real=0.0, imag=0.0):
    """Form a complex number.

    This function is not complete.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        # TODO: implement complex_zero
        return complex_zero
    ...