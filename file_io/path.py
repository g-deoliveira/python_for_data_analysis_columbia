import os

# get current working directory
cwd = os.getcwd()
print(cwd)

# this path points to a file in the current directory
path = "myfile.csv"

# this path points to a file one directory above
path = "../myfile.csv"

# this path points to a file two directories above
path = "../../myfile.csv"

# this path points to a file one directory
# above in an adjacent directory
path = "../other_directory/myfile.csv"

# this is an absolute path (it starts with /)
path = "/Users/UserName/Documents/Columbia/Python/data/myfile.csv"