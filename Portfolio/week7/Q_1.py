# 1. Write and test a function that takes a string as a parameter and returns a sorted list
# of all the unique letters used in the string. So, if the string is cheese, the list
# returned should be ['c', 'e', 'h', 's'].


def unique_letters(string):
    # Use set remove duplicates, then convert it to a list
    letters_list = list(set(string))
    
    # Sort the list
    sort_unique_letters = sorted(letters_list)
    
    return sort_unique_letters

# Get user input
input_string = input("Enter a string: ")

# function call
result = unique_letters(input_string)

# display output
print(f"Unique letters in '{input_string}': {result}")
