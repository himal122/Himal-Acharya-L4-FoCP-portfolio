# 4. Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# get user input
pw_1 = input("Enter a new password (8-12 characters): ")
pw_2 = input("Enter the password again: ")

if (8 <= len(pw_1) <= 12) and (8 <= len(pw_2) <= 12) and (pw_1 not in BAD_PASSWORDS) and (pw_1 == pw_2):
    print("Password set successfully!")

else:
    print("Password do not meet the constraints, please try again!")