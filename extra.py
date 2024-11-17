import os

# Check if the file is writable
if os.access("todos.db", os.W_OK):
    print("The database file is writable.")
else:
    print("The database file is not writable.")
