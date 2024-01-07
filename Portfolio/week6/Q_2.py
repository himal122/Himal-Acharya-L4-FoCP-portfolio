# 2. Write and test a function that takes an integer as its parameter and returns the
# factors of that integer. (A factor is an integer which can be multiplied by another to
# yield the original).

def factors_of_int(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# example useage and display output
num = int(input("Enter an integer: "))
result_factors = factors_of_int(num)
print(f"The factors of {num} are: {result_factors}")
