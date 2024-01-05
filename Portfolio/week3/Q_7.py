# 7. Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive.

# get user input
times_table = int(input("Enter the number for times table (0-12): "))


if 0 <= times_table <= 12:
    for i in range(13):
        print(f"{i} x {times_table} = {i * times_table}")
else:
    print("Error: Please enter a number between 0 and 12.")