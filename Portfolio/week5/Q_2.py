# 2. Write a program that, when run from the command line, reports how many
# arguments were provided. (Remember that the program name itself is not an
# argument).

# Importing sys module to access the command line arguments
import sys

# The sys.argv list contains the program name and the arguments
num_args = len(sys.argv) - 1


print(f"arguments provided: {num_args}")