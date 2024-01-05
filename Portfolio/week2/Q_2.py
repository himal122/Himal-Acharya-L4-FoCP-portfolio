# 2. Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
# Enter a temperature in Celsius: 32.5
# 32.5C is equivalent to 90.5F.


# get user input
get_celsius_tempreture = float(input("Enter a temperature in Celsius: "))

# converting celsius to fahrenheit
fahrenheit_temp = (9/5) * get_celsius_tempreture + 32

# displaying output
print(f"{get_celsius_tempreture}C is equivalent to {fahrenheit_temp}F.")