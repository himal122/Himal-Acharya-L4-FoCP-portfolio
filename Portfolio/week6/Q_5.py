# 5. Another way to hide a message is to include the letters that make it up within
# seemingly random text. The letters of the message might be every fifth character,
# for example. Write and test a function that does such encryption. It should
# randomly generate an interval (between 2 and 20), space the message out
# accordingly, and should fill the gaps with random letters. The function should
# return the encrypted message and the interval used.
# For example, if the message is "send cheese", the random interval is 2, and for
# clarity the random letters are not random:
# send cheese
# s e n d c h e e s e
# sxyexynxydxy cxyhxyexyexysxye

import random
import string

def encrypt_message():
    # Ask the user for a message
    message = input("Please enter a message: ")

    # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)

    # Initialize the encrypted message
    encrypted_message = ""

    # Iterate over each character in the message
    for char in message:
        # If the character is a space, add it to the encrypted message
        if char == " ":
            encrypted_message += char
        else:
            # Add the character and fill the gaps with random letters
            encrypted_message += char + ''.join(random.choice(string.ascii_lowercase) for _ in range(interval))

    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted_message}")
    print(f"Interval used: {interval}")

# Call the function
encrypt_message()
