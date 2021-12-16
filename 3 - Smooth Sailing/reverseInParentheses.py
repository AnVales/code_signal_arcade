# Write a function that reverses characters in (possibly nested) parentheses in the input string.
# Input strings will always be well-formed with matching ()s.

inputString_1 = ""
inputString_2 ="bar"
inputString_3 = "(bar)"
inputString_4 = "foo(bar)baz"
inputString_5 = "foo(bar)baz(blim)"
inputString_6 = "foo(bar(baz))blim"

import re

def solution(inputString): 
    # Patron que buscamos -> (letras)
    pattern = '(\([a-z]*\))'

    if re.findall(pattern, inputString):
        
        for i in re.findall(pattern, inputString):
            inputString = re.sub(i, i[1:-1][::-1], inputString)
        return inputString #solution(inputString)

    else:
        return inputString


print(solution(inputString_5))