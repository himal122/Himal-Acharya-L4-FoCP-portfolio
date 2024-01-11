# 2. The Unix diff command compares two files and reports the differences, if any.
# Write a simple implementation of this that takes two file names as command-line
# arguments and reports whether or not the two files are the same. (Define "same" as
# having the same contents.)


import sys

def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()

            if content1 == content2:
                print(f"The contents of {file1} and {file2} are the same.")
            else:
                print(f"The contents of {file1} and {file2} are different.")
    except FileNotFoundError:
        print("Error: One or both files not found.")

# Check if the command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python Q_2.py <demo_file1_for_q2.txt> <demo_file2_for_q2.txt>")
else:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    compare_files(file1, file2)