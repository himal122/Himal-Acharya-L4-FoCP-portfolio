# 6. Write a program that takes a centigrade temperature and displays the equivalent in
# fahrenheit. The input should be a number followed by a letter C. The output should
# be in the same format.

input_str = input("Enter the temperature in centigrade (e.g., 20C): ")
temperature_celsius = float(input_str[:-1])
unit = input_str[-1].upper()

if unit == 'C':
    # Converting Celsius to Fahrenheit
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    print(f"{temperature_celsius:.2f}C is equivalent to {temperature_fahrenheit:.2f}F")
else:
    print("Invalid input. Please use the format 'numberC'.")
