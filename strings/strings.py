
"""enclosed in triple quotes (double)"""
'''enclosed in triple quotes (single)'''
"enclosed in standard quotes (double)"
'enclosed in standard quotes (single)'

text = "Escaped double quote\"."
text = 'Escaped single quote\'.'
text = 'Sentence 1.\nSentence 2.'
text = 'Token 1\ttab\ttab\tToken 2'

text = "Hello world."
assert text[0] == "H"
assert "e" == text[1]
assert text[-1] == "."

assert text[:3] == "Hel"
assert text[-3:] == "ld."

assert text[::2] == "Hlowrd"

assert text[::-1] == ".dlrow olleH"
assert text[::-2] == ".lo le"

assert "H" in text
assert "h" not in text

assert "Hello" in text
assert "xyz" not in text

assert len("") == 0
assert len("H") == 1
assert len(text) == 12

assert "a" 'b' """cde""" == "abcde"

text = (
    "This separated string "
    "becomes one."
)
assert text == "This separated string becomes one."

space_separated_list = [
    "a"
    "b"
    "c"
]

comma_separated_list = [
    "a",
    "b",
    "c",
]

assert len(space_separated_list) == 1
assert len(comma_separated_list) == 3
