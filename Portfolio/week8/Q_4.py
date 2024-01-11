# 4. The Unix wc command counts the number of lines, words, and characters in a file.
# Write an implementation of this that takes a file name as a command-line
# argument, and then prints the number of lines and characters.
# Note: Linux (and Mac) users can use the "wc" command to check the results of their
# implementation.


import sys

def wc(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            char_count = sum(len(line) for line in lines)

            print(f"Lines: {line_count}")
            print(f"Characters: {char_count}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Check if the command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: python Q_4.py <demo_file_for_q4.txt>")
else:
    file_name = sys.argv[1]
    wc(file_name)
