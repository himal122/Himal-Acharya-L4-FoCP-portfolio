import os
import getpass
from common_functions import encryption, check_current_username, is_lowercase
from adduser import add_user
from deluser import delete_user
from passwd import change_password
from login import login

def main():
    print("\nWelcome to the User Management System!")
    print("-------------------------------------")

    # Prompts the user to enter a command from the given options
    commands = input("\nCommands:\n\n"
                      "1. Add User\n"
                      "2. Login\n"
                      "3. Change Password\n"
                      "4. Delete User\n\n"
                      "Enter a command: ").strip().lower()

    # Process the user's choice
    if commands == "add user" or commands == '1':
        add_new_user()
    elif commands == "login" or commands == '2':
        execute_login()
    elif commands == "change password" or commands == '3':
        execute_password_change()
    elif commands == "delete user" or commands == '4':
        delete_existing_user()
    else:
        print(f"Invalid command! Please choose a valid option.")

def add_new_user():
    # Prompts the user to enter a new username and validates
    while True:
        username = input("Enter new username: ")
        if not is_lowercase(username):
            print("Invalid username. Must be in lowercase letters and valid string.")
        else:
            break

    # Prompts the user to enter the real name
    real_name = input("Enter real name: ")

    # Prompts the user to enter a password and validates
    while True:
        password = input("Enter password: ")
        if len(password) >= 8:
            password = encryption(password)
            break
        else:
            print("Password must be at least 8 characters long.")

    # Adds the new user with the user's information
    add_user(username, real_name, password)

def execute_login():
    # Prompts the user to enter their username and password for login
    while True:
        username = input("Enter username: ")
        password = encryption(getpass.getpass("Enter password: "))

        # Checks if the provided username and password is correct
        if login(username, password):
            print("Access granted.")
            break
        else:
            print("Access denied.")

def execute_password_change():
    # Prompts the user to enter the username to change the password
    while True:
        username = input("Enter username: ")
        if not is_lowercase(username):
            print("Invalid username. Must be in lowercase letters.")
        elif not check_current_username(username):
            print("Username not found. Please enter a valid username.")
        else:
            break

    # Prompts the user to enter the current password for verification
    current_password = encryption(getpass.getpass("Enter current password: "))

    # Prompts the user to enter a new password and validates
    while True:
        new_password = encryption(getpass.getpass("Enter new password: "))
        if len(new_password) >= 8:
            break
        else:
            print("New password must be at least 8 characters long.")

    # Prompts the user to confirm the new password
    confirm_password = encryption(getpass.getpass("Confirm new password: "))

    # Checks if the new password matches the confirmed password and changes it
    if new_password == confirm_password:
        change_password(username, current_password, new_password)
    else:
        print("Passwords do not match. Nothing changed.")

def delete_existing_user():
    # Prompts the user to enter the username of the user to be deleted
    while True:
        username = input("Enter username to delete: ")
        if not is_lowercase(username):
            print("Invalid username. Must be in lowercase letters and valid string.")
        else:
            break
    # Delete the user with the provided username
    delete_user(username)

# Check if the password file exists
if not os.path.exists('passwd.txt'):
    print("File not found.")
else:
    try:
        # Start the main program
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        
