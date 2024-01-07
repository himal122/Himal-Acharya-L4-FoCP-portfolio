# 3. Write and test a function that determines if a given integer is a prime number. A
# prime number is an integer greater than 1 that cannot be produced by multiplying
# two other integers.


def prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# example useage and display output
num = int(input("Enter an integer: "))
if prime_number(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

