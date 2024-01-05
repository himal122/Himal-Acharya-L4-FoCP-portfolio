# 4. When processing data it is often useful to remove the last character from some
# input (it is often a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)


def remove_last_char(input_string):
    # Checking if the string has one or fewer characters
    if len(input_string) <= 1:
        return input_string

    # Remove the last character
    return input_string[:-1]

# Testing the function
test_string = input("Enter a string: ")
result = remove_last_char(test_string)

print(f"Original string: {test_string}")
print(f"String with the last character removed: {result}")
