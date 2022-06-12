# You are taking part in an Escape Room challenge designed specifically for programmers. 
# In your efforts to find a clue, you've found a binary code written on the wall behind a vase,
#  and realized that it must be an encrypted message. 
# After some thought, 
# your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

# Assuming that your hunch is correct, decode the message.

import re

def solution(code):
    # Separate every 8 characters
    a_binary_list = re.findall('.{8}',code)

    # Convert to base 2 decimal integer
    ascii_string = ""
    for binary_value in a_binary_list:
        an_integer = int(binary_value, 2)

        # Convert to ASCII character
        ascii_character = chr(an_integer)

        # Append character to `ascii_string`
        ascii_string += ascii_character

    return(ascii_string)
