# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

import re

# Solution function
def solution(inputString): 

    # Pattern -> (letters)
    pattern = '(\([a-z]*\))'

    # If it finds the patters:
    if re.findall(pattern, inputString):
        
        # Replace with the reverse without () the pattern
        for i in re.findall(pattern, inputString):
            inputString = inputString.replace(i, i[1:-1][::-1])
        return solution(inputString)

    else:
        return inputString
