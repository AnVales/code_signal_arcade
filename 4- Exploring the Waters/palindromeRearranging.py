# Given a string, find out if its characters can be rearranged to form a palindrome.

# Solution function
def solution(inputString):

    # Dictionary with the letters of the input string and a counter of letters
    dict_letter = {}
    counter = 0

    for letter in inputString:
        counter = counter + 1
        if not letter in dict_letter.keys():
            dict_letter[letter] = 1

        else:
            dict_letter[letter] = dict_letter[letter] + 1
        
    # Check if the input string is odd or even
    letters_odd = 0
    counter_even = False

    for letter in dict_letter.keys():
        if not dict_letter[letter] % 2 == 0:
            letters_odd = letters_odd + 1

    if counter % 2 == 0:
        counter_even = True
        
    # Check palindrome
    if counter_even and letters_odd == 0:
        return True
    elif not counter_even and letters_odd == 1:
        return True
    else: 
        return False
