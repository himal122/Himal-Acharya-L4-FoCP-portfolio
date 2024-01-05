# 5. Modify your program a final time so that it executes until the user successfully
# chooses a password. That is, if the password chosen fails any of the checks, the
# program should return to asking for the password the first time.

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


# using loop to keep asking for password
while True:

    # get user input
    pw_1 = input("Enter a new password (8-12 characters): ")
    pw_2 = input("Enter the password again: ")

    if (8 <= len(pw_1) <= 12) and (8 <= len(pw_2) <= 12) and (pw_1 not in BAD_PASSWORDS) and (pw_1 == pw_2):
        print("Password set successfully!")
        break
    
    else:
        print("Password do not meet the constraints, please try again!")