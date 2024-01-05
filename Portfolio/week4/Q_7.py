# 7. Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.
# Hint: You should know there are built-in functions for max and min. If you hunt, you
# might also find one for the mean.


temperatures = []

for i in range(6):
    input_str = input(f"Enter temperature {i + 1} in centigrade (e.g., 20C): ").upper()

    if input_str[:-1].isdigit() and input_str.endswith('C'):
        temperatures.append(float(input_str[:-1]))
    else:
        print(f"invalid input: {input_str}. Please use the format 'numberC'.")

if temperatures:
    print(f"Maximum temperature: {max(temperatures):.2f}C")
    print(f"Minimum temperature: {min(temperatures):.2f}C")
    print(f"Mean temperature: {sum(temperatures) / len(temperatures):.2f}C")
else:
    print("No valid temperatures entered.")
