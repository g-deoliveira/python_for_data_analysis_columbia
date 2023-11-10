data = "Title"

# write to a file in the same directory
file_name = "file.extension"
with open(file_name, "w") as fh:
    fh.writelines(data)

data = ["\nSubtitle", "\nThe contents."] # notice the line breaks
# append data to the same file
with open(file_name, "a") as fh:
    fh.writelines(data)

# now read the data from the file
data_io = ""
with open(file_name, "r") as fh:
    for line in fh:
        data_io += line

assert data_io == "Title\nSubtitle\nThe contents."