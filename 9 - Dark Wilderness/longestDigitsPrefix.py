# Given a string, output its longest prefix which contains only digits.

# Solution function
def solution(inputString):
    import re

    # Search the first digits
    output = re.search('^\d*', inputString)

    return(output.group())
