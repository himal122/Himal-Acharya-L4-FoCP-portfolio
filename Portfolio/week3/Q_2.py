# . Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error.

# get user input
pw_1 = input("Enter a new password: ")
pw_2 = input("Enter the password again: ")

if pw_1 == pw_2:
    print("Password set successfully!")

else:
    print("Password do not match, please try again!")