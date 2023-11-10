import json

book = {
    "title": "Clean Code",
    "author": "R. Martin",
    "year": 2008,
}

# writing the contents of the book dictionary to a json file
# note the contents are written on one line, which isn't
# very easy to read
with open("file_io/my_file_one_line.json", "w") as file:
    json.dump(book, file)

# specify a value of the indent parameter to "prettify" the output
with open("file_io/my_file_one_line.json", "w") as file:
    json.dump(book, file, indent=4)

# read the contents of the json file:
with open("file_io/my_file_one_line.json", "r") as file:
    data = json.load(file)

assert data == book

# now convert a dictionary to a json-string notation
book_as_string = json.dumps(book)
assert (
    book_as_string
    == '{"title": "Clean Code", "author": "R. Martin", "year": 2008}'
)

# now convert the json-string variable to a dictionary
book_from_string = json.loads(book_as_string)
assert book_from_string == book
