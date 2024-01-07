# 4. Computers are commonly used in encryption. A very simple form of encryption
# (more accurately "obfuscation") would be to remove the spaces from a message
# and reverse the resulting string. Write, and test, a function that takes a string
# containing a message and "encrypts" it in this way.

def simple_encryption(message):
    # Remove spaces from the message
    message_without_spaces = message.replace(" ", "")
    
    # Reverse string
    encrypted_message = message_without_spaces[::-1]
    
    return encrypted_message

# example useage and display output
input_message = input("Enter a message: ")
encrypted_result = simple_encryption(input_message)
print(f"The encrypted message is: {encrypted_result}")
