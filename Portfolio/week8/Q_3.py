# 3. The Unix grep command searches a file and outputs the lines in the file that
# contain a certain pattern. Write an implementation of this. It will take two
# command-line arguments: the first is the string to look for, and the second is the
# file name. The output should be the lines in the file that contain the string.

import sys

def grep(string_to_find, file_name):
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if string_to_find in line:
                    print(f"{file_name}:{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")


# Check if the command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python Q_3.py <'demo'> <demo_file_for_q3.txt>")
else:
    string_to_find = sys.argv[1]
    file_name = sys.argv[2]
    grep(string_to_find, file_name)
