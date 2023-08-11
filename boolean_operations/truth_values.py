
# all of these evaluate to False
bool(0)
bool(0.0)
bool(None)
bool('') # empty string (using single quotes)
bool("") # empty string (using double quotes)
bool([]) # empty list
bool(()) # empty tuple

# all of these evaluate to True
bool(True)
bool(3)
bool('cat')
bool(' ') # non-empty string
bool([0]) # non-empty list
