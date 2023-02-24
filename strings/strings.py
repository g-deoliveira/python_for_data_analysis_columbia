
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

assert "xyz" + "abc" == "xyzabc"
assert "abc" * 2 == "abcabc"
assert 2 * "abc" == "abcabc"

assert "a" 'b' """cde""" == "abcde"

text = (
    "This separated string " # context comment
    "becomes one."
)
assert text == "This separated string becomes one."

my_list = [
    "cat",
    "dog"   # oops forgot a comma here
    "fish",
    "bird",
]

assert my_list == ["cat", "dogfish", "bird"]

