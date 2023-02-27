import os

# Set the directory path
dir_path = '.'

# Get the names of all files in the directory (excluding subdirectories)
file_names = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# Remove the file extensions and print the names
for file_name in file_names:
    name_without_ext, ext = os.path.splitext(file_name)
    print(name_without_ext)
