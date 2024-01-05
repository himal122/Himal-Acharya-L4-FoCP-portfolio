# 1. Functions are often used to validate input. Write a function that accepts a single
# integer as a parameter and returns True if the integer is in the range 0 to 100
# (inclusive), or False otherwise. Write a short program to test the function.


# defining a simple function
def single_int(num):
    return 0 <= num <= 100

# Test the function
test_number = int(input("Enter an integer: "))
result = single_int(test_number)

if result:
    print("True")
else:
    print("False")
