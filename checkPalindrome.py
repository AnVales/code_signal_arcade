# Given the string, check if it is a palindrome.
# A string that doesn't changed when reversed (it reads the same backward and forward).

def checkPalindrome(inputString):
    
    reverse_string = inputString[::-1]
    
    return inputString == reverse_string
