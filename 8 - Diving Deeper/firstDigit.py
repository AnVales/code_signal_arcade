# Find the leftmost digit that occurs in a given string.

# Solution function
def solution(inputString):
    import re

    #returns first digit
    outputArray = re.findall('[0-9]', inputString)
    return(outputArray[0])