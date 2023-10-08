# capitalize()
text = "python for data analysis"
assert text.capitalize() == "Python for data analysis"

# text.capitalize() returns a new string but does not replace it
# to replace the string, you have to overwrite it:
text = text.capitalize()
assert text == "Python for data analysis"

# lower
text = "XYZ 123 !?/fgh"
assert text.lower() == "xyz 123 !?/fgh"

# text.lower() returns a new string but does not replace it
# to replace the string, you have to overwrite it:
text = text.lower()
assert text == "xyz 123 !?/fgh"

# upper
text = "XYZ 123 !?/fgh"
assert text.upper() == "XYZ 123 !?/FGH"

# text.upper() returns a new string but does not replace it
# to replace the string, you have to overwrite it:
text = text.upper()
assert text == "XYZ 123 !?/FGH"

# lstrip
text = "Random Forest"
assert text.lstrip("RFas123t") == "ndom Forest"
assert text.lstrip("st") == "Random Forest"
assert text.lstrip("Ra") == "ndom Forest"
assert text.lstrip("xyz") == "Random Forest"
assert text.lstrip() == "Random Forest"

# rstrip
text = "Random Forest"
assert text.rstrip("RFas123t") == "Random Fore"
assert text.rstrip("st") == "Random Fore"
assert text.rstrip("Ra") == "Random Forest"
assert text.rstrip("xyz") == "Random Forest"
assert text.rstrip() == "Random Forest"

# strip
text = "Random Forest"
assert text.strip("RFas123t") == "ndom Fore"
assert text.strip("st") == "Random Fore"
assert text.strip("Ra") == "ndom Forest"
assert text.strip("xyz") == "Random Forest"
assert text.strip() == "Random Forest"

# replace
text = "Random Forest"
assert text.replace("o", "_") == "Rand_m F_rest"
assert text.replace("o", "_", 1) == "Rand_m Forest"
assert text.replace("Random ", "") == "Forest"

# removeprefix
text = "Random Forest"
assert text.removeprefix("RFas123t") == "Random Forest"
assert text.removeprefix("st") == "Random Forest"
assert text.removeprefix("Ra") == "ndom Forest"
assert text.removeprefix("xyz") == "Random Forest"

# removesuffix
text = "Random Forest"
assert text.removesuffix("RFas123t") == "Random Forest"
assert text.removesuffix("st") == "Random Fore"
assert text.removesuffix("Ra") == "Random Forest"
assert text.removesuffix("xyz") == "Random Forest"

# zfill
text = "123"
assert text.zfill(1) == "123"
assert text.zfill(2) == "123"
assert text.zfill(3) == "123"
assert text.zfill(4) == "0123"
assert text.zfill(5) == "00123"
text = "+123"
assert text.zfill(6) == "+00123"

# format
text = "{} + {}"

# using positional parameters
assert text.format(2, 3) == "2 + 3"
assert text.format("cat", "dog") == "cat + dog"

# using the numeric index
text = "{0} + {1}"
assert text.format(2, 3) == "2 + 3"
assert text.format("cat", "dog") == "cat + dog"

# using the name of the keyword argument
text = "{x} + {y}"
assert text.format(x=2, y=3) == "2 + 3"

# count
text = "Random Forest"
assert text.count("Ra") == 1
assert text.count("o") == 2
assert text.count("o", 1, 5) == 1
assert text.count("o", 1, 4) == 0
assert text.count("Z") == 0

# index
text = "Random Forest"
assert text.index("R") == 0
assert text.index("o") == 4
assert text.index("o", 1, 5) == 4
assert text.index("o", 5) == 8


# find
assert text.find("R") == 0
assert text.find("o") == 4
assert text.find("o", 1, 5) == 4
assert text.find("o", 5) == 8
assert text.find("XYZ") == -1

# isalpha
assert not "abc DEF".isalpha() # white space
assert "abcDEF".isalpha() # no white space

# isdecimal
assert "12345".isdecimal()
assert not "123 45".isdecimal() # white space
assert "1".isdecimal()
assert not "".isdecimal() # at least one character
assert not "x".isdecimal()

# isnumeric
assert "12345".isnumeric()
assert not "123 45".isnumeric() # white space
assert "1".isnumeric()
assert not "".isnumeric() # at least one character
assert not "x".isnumeric()

# isalnum
assert "12345".isalnum()
assert not "123 45".isalnum() # white space
assert "1".isalnum()
assert not "".isalnum() # at least one character
assert "x".isalnum()
assert "1x2x3x4x5".isalnum()

# islower
assert not "PYTHON".islower()
assert "python".islower()
assert "r".islower()
assert not "R".islower()

# isupper
assert "PYTHON".isupper()
assert not "python".isupper()
assert not "r".isupper()
assert "R".isupper()

# startswith
assert "abc".startswith("a")
assert not "abc".startswith("b")

# endswith
assert "abc".endswith("c")
assert not "abc".endswith("b")

# join
iterable = ["Good", "day!"]
assert ",".join(iterable) == "Good,day!"
assert ", ".join(iterable) == "Good, day!"
assert "".join(iterable) == "Goodday!"

# split
assert "Good day!".split() == ["Good", "day!"]
assert "Good day!".split(" ") == ["Good", "day!"]
assert "Good day!".split("d") == ["Goo", " ", "ay!"]
assert "Good day!".split(" day") == ["Good", "!"]


