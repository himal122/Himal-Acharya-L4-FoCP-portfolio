import codecs

# constant for passwd file
PASSWORDS_FILE = 'passwd.txt'

def check_current_username(username):
    """
    Check if a username already exists in the password file.
    Parameters:
    - username (str): The username to check.
    Returns:
    - bool: True if the username exists, False if the username doesn't exist.
    """
    try:
        with open(PASSWORDS_FILE, 'r') as file:
            # Reads each line in the password file
            for line in file:
                # Splits the line into parts based on ':'
                part = line.split(':')
                # Checks if the first part (username) matches the user's entered username
                if part[0] == username:
                    return True
        return False
    except FileNotFoundError:
        print("Password file not found.")
        return False
    except PermissionError:
        print("Permission denied to access password file.")
        return False

# NOT CURRENTLY IN USE ON ANY OTHER MODULES

# def write_in_PASSWORDS_FILE(lines):
#     """
#     Write lines to the password file.
#     Parameters:
#     - lines (list): List of lines to write to the password file.
#     """
#     try:
#         with open(PASSWORDS_FILE, 'w') as file:
#             # Writes the provided lines to the password file
#             file.writelines(lines)
#     except FileNotFoundError:
#         print("Password file not found.")
#     except PermissionError:
#         print("Permission denied to access password file.")
    


def encryption(text):
    """
    Encrypts text using ROT13.
    Parameters:
    - text (str): The text to be encrypted.
    Returns:
    - str: The encrypted text.
    """
    return codecs.encode(text, 'rot_13')

def is_lowercase(username):
    """
    Check if a username is in lowercase.
    Parameters:
    - username (str): The username to check.
    Returns:
    - bool: True if the username is in lowercase, False otherwise.
    """
    return username.islower()
