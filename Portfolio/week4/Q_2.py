# 2. Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.


# defining a function to count upper and lower case in a string
def count_upper_lower(input_string):
    # Initialize counters
    upper_count = 0
    lower_count = 0

    # Count uppercase and lowercase letters
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Test the function
test_string = input("Enter a string: ")
upper_count, lower_count = count_upper_lower(test_string)

print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
