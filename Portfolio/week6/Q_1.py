# 1. Write a function that accepts a positive integer as a parameter and then returns a
# representation of that number in binary (base 2).
# Hint: This is in many ways a trick question. Think!

# get input
def user_input():
    num = int(input("Enter a positive integer: "))
    return num

# convert decimal to binary
def decimal_to_binary(positive_int):
    return bin(positive_int)

# display output
def display_output(decimal_input, binary_representation):
    print(f"The binary representation of {decimal_input} is: {binary_representation}")


decimal_number = user_input()
binary_representation = decimal_to_binary(decimal_number)
display_output(decimal_number, binary_representation)
