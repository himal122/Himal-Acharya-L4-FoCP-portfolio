# 3. Write a program that takes a bunch of command-line arguments, and then prints
# out the shortest. If there is more than one of the shortest length, any will do.
# Hint: Don't overthink this. A good way to find the shortest is just to sort them.


import sys

# ignore the first element, which is the program name
args = sys.argv[1:]

# check if there are any arguments
if not args:
    print("No command-line arguments provided.")
else:
    # sort the arguments by ascending order
    args.sort(key=len)

    # print the first element of the sorted list
    print(f"The shortest argument is {args[0]}.")
