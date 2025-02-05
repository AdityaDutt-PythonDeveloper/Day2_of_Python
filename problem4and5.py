import os

# Specify the directory path; use '.' for the current directory
directory_path = '/'

# Get the list of all files and directories
entries = os.listdir(directory_path)

# Print the list
for entry in entries:
    print(entry)
