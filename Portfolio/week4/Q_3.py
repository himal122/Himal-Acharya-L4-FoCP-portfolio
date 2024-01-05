# 3. Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name differently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur.



# getting user input and formatting it to Capitalize the name
get_users_name = input("Hello, what is your name? ").capitalize()

# displaying output
if not get_users_name:
    print("Hello, Stranger!")
else:
    print(f"Hello, Mr/Mrs {get_users_name}. Good to meet you!")