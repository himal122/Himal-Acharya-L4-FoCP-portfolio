# 5. Last week you wrote a program that processed a collection of temperature readings
# entered by the user and displayed the maximum, minimum, and mean. Create a
# version of that program that takes the values from the command-line instead. Be
# sure to handle the case where no arguments are provided!


import sys

temperatures = []

# Check if command-line arguments are provided
if len(sys.argv) < 2:
    print("No temperatures provided. Please use the format 'numberC' as command-line arguments.")
    sys.exit(1)

# Process command-line arguments
for i in range(1, len(sys.argv)):
    input_str = sys.argv[i].upper()

    if input_str[:-1].isdigit() and input_str.endswith('C'):
        temperatures.append(float(input_str[:-1]))
    else:
        print(f"Invalid input: {sys.argv[i]}. Please use the format 'numberC'.")

if temperatures:
    print(f"Maximum temperature: {max(temperatures):.2f}C")
    print(f"Minimum temperature: {min(temperatures):.2f}C")
    print(f"Mean temperature: {sum(temperatures) / len(temperatures):.2f}C")
else:
    print("No valid temperatures entered.")
