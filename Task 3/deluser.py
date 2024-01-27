from common_functions import PASSWORDS_FILE

def delete_user(username):
    """
    Delete a user from the password file.
    Parameters:
    - username (str): The username to be deleted.
    """
    # Reads all lines from the password file
    with open(PASSWORDS_FILE, 'r') as file:
        lines = file.readlines()

    # Flag to track if the user is deleted
    user_deleted = False
    
    # Opens the password file in write mode
    with open(PASSWORDS_FILE, 'w') as file:
        # Iterates through each line in the original file
        for line in lines:
            # Checks if the line does not start with the username to be deleted
            if not line.startswith(f"{username}:"):
                # If not, writes the line to the new file
                file.write(line)
            else:
                # If the line starts with the username, mark user_deleted as True
                user_deleted = True

    # Checks if the user was successfully deleted and print message
    if user_deleted:
        print(f"User '{username}' deleted successfully!")
    else:
        print("User not found. Nothing changed.")
        