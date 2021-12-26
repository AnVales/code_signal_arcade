# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

import re

def solution(inputString): 
    # Patron que buscamos -> (letras)
    pattern = '(\([a-z]*\))'

    # Si hay patron:
    if re.findall(pattern, inputString):
        
        # Reemplaza por el inverso sin patron
        for i in re.findall(pattern, inputString):
            inputString = inputString.replace(i, i[1:-1][::-1])
        return solution(inputString)

    else:
        return inputString
