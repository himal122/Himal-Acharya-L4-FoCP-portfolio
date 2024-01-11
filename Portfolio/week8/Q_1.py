# 1. The Unix nl command prints the lines of a text file with a line number at the start
# of each line. (It can be useful when printing out programs for dry runs or white-box
# testing). Write an implementation of this command. It should take the name of the
# files as a command-line argument.


import sys

def nl(file_name):
    try:
        with open(file_name, 'r') as file:
            line_number = 1
            for line in file:
                print(f"{line_number}\t{line.strip()}")
                line_number += 1
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")


# Check if the command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: python Q_1.py <demo_file_for_q1.txt>")
else:
    filename = sys.argv[1]
    nl(filename)
