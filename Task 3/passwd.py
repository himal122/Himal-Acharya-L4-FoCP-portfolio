from common_functions import PASSWORDS_FILE

def change_password(username, current_password, new_password):
    """
    Change the password for a user in the password file.
    Parameters:
    - username (str): The username for which the password is to be changed.
    - current_password (str): The current password to be verified.
    - new_password (str): The new password to be set.
    """

    # Opens the password file in read mode to read existing passwords
    with open(PASSWORDS_FILE, 'r') as file:
        # Reads all lines from the file
        lines = file.readlines()
    
    # Flag to track if the password has been successfully changed
    password_changed = False
    
    # Opens the password file in write mode 
    with open(PASSWORDS_FILE, 'w') as file:
        # Iterates through each line in the file
        for line in lines:
            # Checks if the line matches the username and current password
            if line.startswith(f"{username}:") and line.endswith(f":{current_password}\n"):
                # If it matches, write the new password
                file.write(f"{username}:{line.split(':')[1]}:{new_password}\n")
                # Sets the flag to indicate successful password change
                password_changed = True
            else:
                # Otherwise, write the line as is
                file.write(line)

    # Checks if the password was successfully changed
    if password_changed:
        print("Password changed.")
    else:
        print("Current password is incorrect. Nothing changed.")
        
