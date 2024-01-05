# 3. Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.

# get user input
pw_1 = input("Enter a new password (8-12 characters): ")
pw_2 = input("Enter the password again: ")

if (8 <= len(pw_1) <= 12) and (8 <= len(pw_2) <= 12) and (pw_1 == pw_2):
    print("Password set successfully!")

else:
    print("Password do not meet the length or do not match, please try again!")
