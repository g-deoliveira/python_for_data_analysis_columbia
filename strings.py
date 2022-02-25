
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

# built-in methods that transform
text = " Hello how are you? "

assert text.lower() == ' hello how are you? '
assert text.upper() == ' HELLO HOW ARE YOU? '
# remove leading spaces
assert text.lstrip() == "Hello how are you? "
# remove trailoing spaces
assert text.rstrip() == " Hello how are you?"
# remove leading and trailing spaces
assert text.strip() == "Hello how are you?"

# fill in with 0s (useful for zip codes for instance)
zip_code = '123'
assert zip_code.zfill(5) == '00123'

# boolean questions
address = '123 Main St. Apt 100'
assert address.startswith('123 Main')
assert address.endswith('Apt 100')

street_number = address[:3]
assert street_number == '123'
isalpha = street_number.isalpha()
assert not isalpha

isnumeric = street_number.isnumeric()
assert isnumeric


# built-in methods that work with substrings
text = "They have one dog, one cat and four fish."

assert text.count("one") == 2

# if the substring is not found, find returns -1
# otherwise it returns the index of the substring
assert text.find("one") == 10
assert text.find("two") == -1

# if the substring is not found, index raises
# a ValueError, otherwise it returns the index
assert text.index("one") == 10
try:
    two = text.index("two")
except ValueError as ve:
    print(ve)
    assert str(ve) == "substring not found"

# replace(old, new): replace old with new
old = "dog"
new = "Labrado"
text.replace(old, new) == "They have one Labrador, one cat and four fish."

# chaining string methods together
text = "   Hello how are you?"

assert text.strip().startswith("Hello")
assert text.strip().upper()[:5] == "HELLO"

