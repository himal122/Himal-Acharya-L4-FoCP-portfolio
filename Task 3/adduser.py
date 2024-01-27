from common_functions import PASSWORDS_FILE, check_current_username

def add_user(username, real_name, password):
    """
    Add a new user to the password file if the username does not exist.
    Parameters:
    - username (str): The username to be added.
    - real_name (str): The real name associated with the username.
    - password (str): The password for the new user.
    """
    # Checks if the username already exists
    if check_current_username(username):
        print("Cannot add. Most likely username already exists.")
    else:
        # If the username doesn't exist, append the user details to the password file
        with open(PASSWORDS_FILE, 'a') as file:
            file.write(f"{username}:{real_name}:{password}\n")
        print("User Created.")
        