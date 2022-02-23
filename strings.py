
# these are all equivalent
pet = 'cat'
pet = "cat"
pet = '''cat'''
pet = """cat"""

# your string contains single quotes
# (define the string using double quotes)
quote = "And then he said, 'No soup for you!'"

# your string contains double quotes
# (define the string using single quotes)
quote = 'And then he said, "No soup for you!"'

# alternatively, use the escape key (\) to escape
# the single or double quotes
quote = 'And then he said, \'No soup for you!\''
print(quote)

# triple quotes wrap text over multiple lines
# and preserve the line breaks
triple = """select *
from employees
where employee_id = 123
"""
assert triple == 'select *\nfrom employees\nwhere employee_id = 123\n'

# alternatively, use the line break
query = 'select *\nfrom employees\nwhere employee_id = 123\n'
assert query == triple

# accessing characters via indexing and slicing:
pets = "dogs, birds, fish, cats"

assert pets[0] == 'd'
assert pets[-1] == 's'
assert pets[:3] == 'dog'
assert pets[-3:] =='ats'
assert pets[0:8:2] == 'dg,b'
assert pets[::-1] == 'stac ,hsif ,sdrib ,sgod'

assert len(pets) == 23

assert "dog" in pets
assert "horse" not in pets

assert max(pets) == "t"
assert min(pets) == " "

# concatenation
assert "abc" + 'def' == 'abcdef'

# repetition
assert "abc" * 3 == "abcabcabc"