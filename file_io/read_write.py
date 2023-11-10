# open a handle to a file in write mode
file = open("file.txt", "w")

file.write("abc\n")
file.write("def\n")
file.write("\n")
file.write("xyz\n")

file.writelines

# remember to close the file!
file.close()

# now let's read the contents into a list
file = open("file.txt", "r")
data = file.readlines()

assert data == ['abc\n', 'def\n', '\n', 'xyz\n']

# remember to close the file!
file.close()
