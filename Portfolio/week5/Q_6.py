# 6. Write a program that takes the name of a file as a command-line argument, and
# creates a backup copy of that file. The backup should contain an exact copy of the
# contents of the original and should, obviously, have a different name.
# Hint: By now, you should be getting the idea that there is a built-in way to do the
# heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the docs.


import shutil
import sys
import os

def create_backup(original_file):
    # Check if the original file exists
    if not os.path.exists(original_file):
        print(f"Error: The file '{original_file}' does not exist.")
        return

    # Create a backup file name
    backup_file = original_file + ".backup"

    try:
        # Copy the contents of the original file to the backup file
        shutil.copy2(original_file, backup_file)
        print(f"Backup created successfully: {backup_file}")
    except Exception as e:
        print(f"Error creating backup: {e}")


 # Check if the command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: python Q_6.py <demo_file_for_q_no_6.txt>")
else:
    filename = sys.argv[1]
    create_backup(filename)
