# Given a string, output its longest prefix which contains only digits.

def solution(inputString):
    import re

    output = re.search('^\d*', inputString)

    return(output.group())
