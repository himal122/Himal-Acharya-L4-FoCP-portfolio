# 8. Modify the "Times Table" again so that the user still enters the number of the table,
# but if this number is negative the table is printed backwards. So entering "-7"
# would produce the Seven Times Table starting at "12 times" down to "0 times".


# get user input
times_table = int(input("Enter the number for times table (-12 to 0): "))

if -12 <= times_table < 0:
    for i in range(12, -1, -1):
        print(f"{i} x {times_table} = {i * times_table}")

elif 0 <= times_table <= 12:
    for i in range(13):
        print(f"{i} x {times_table} = {i * times_table}")
else:
    print("Error: Please enter a number between -12 and 12.")

