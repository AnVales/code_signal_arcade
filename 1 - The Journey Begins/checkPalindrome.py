# Given the string, check if it is a palindrome.
# A string that doesn't changed when reversed (it reads the same backward and forward).

# Solution function
def solution(inputString):
    # Checks the reverse
    return inputString == inputString[::-1]
