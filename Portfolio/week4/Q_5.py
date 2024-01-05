# 5. Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae).


# defining function
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Testing the functions
celsius_value = float(input("Enter temperature in Celsius: "))
fahrenheit_result = celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value} degrees Celsius is equal to {fahrenheit_result:.2f} degrees Fahrenheit.")

fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
celsius_result = fahrenheit_to_celsius(fahrenheit_value)
print(f"{fahrenheit_value} degrees Fahrenheit is equal to {celsius_result:.2f} degrees Celsius.")
