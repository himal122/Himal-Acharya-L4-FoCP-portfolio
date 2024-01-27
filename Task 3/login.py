from common_functions import PASSWORDS_FILE

def login(username, password):
    """
    Check if a given username and password combination is valid for login.
    Parameters:
    - username (str): The username to be checked.
    - password (str): The password to be checked.
    Returns:
    - bool: True if the combination is valid, False otherwise.
    """
    # Opens the password file in read mode
    with open(PASSWORDS_FILE, 'r') as file:
        # Iterates through each line in the file
        for line in file:
            # Strips newline character and splits the line into parts
            values = line.strip().split(':')
            # Checks if the username and password match the values in the line
            if values[0] == username and values[2] == password:
                # If the combination is valid, returns True
                return True
    # If no valid combination is found, returns False
    return False
