
# recall an assertion generates an exception
# if the condition it evaluates is False

# these generate an AssertionError
assert False
assert None
assert 0
assert 0.0
assert '' # empty string (using single quotes)
assert "" # empty string (using double quotes)
assert [] # empty list
assert () # empty tuple

# these all pass
assert True
assert 3
assert 'cat'
assert ' '
assert [0]
