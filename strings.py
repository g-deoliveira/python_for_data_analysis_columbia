
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
triple = """
select *
from employees
where employee_id = 123
"""
assert triple == '\nselect *\nfrom employees\nwhere employee_id = 123\n'

# alternatively, use the line break
query = 'select *\nfrom employees\nwhere employee_id = 123\n'
assert query == triple

