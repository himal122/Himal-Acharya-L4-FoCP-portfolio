# 8. Modify the previous program so that it can process any number of values. The input
# terminates when the user just pressed "Enter" at the prompt rather than entering a
# value.


temperatures = []

i = 1
while True:
    input_str = input(f"Enter temperature {i} in centigrade (e.g., 20C, press Enter to finish): ").upper()

    if not input_str:
        break  # Exit the loop if the user presses Enter without entering a value

    if input_str[:-1].isdigit() and input_str.endswith('C'):
        temperatures.append(float(input_str[:-1]))
        i += 1
    else:
        print(f"Invalid input: {input_str}. Please use the format 'numberC'.")


if temperatures:
    print(f"Maximum temperature: {max(temperatures):.2f}C")
    print(f"Minimum temperature: {min(temperatures):.2f}C")
    print(f"Mean temperature: {sum(temperatures) / len(temperatures):.2f}C")
else:
    print("No valid temperatures entered.")