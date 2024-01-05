# 1. Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before.

# getting user input
get_users_name = input("Hello, what is your name? ")

# displaying output
if not get_users_name:
    print("Hello, Stranger!")
else:
    print(f"Hello, Mr/Mrs {get_users_name}. Good to meet you!")