# A string is said to be beautiful 
# if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; 
# ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

# Given a string, check whether it is beautiful.

# Solution function
def solution(inputString):
    
    # List with the alphabet
    import string
    alphabet_list = list(string.ascii_lowercase) 

    # A list with the frequencies of each letter
    alphabet_list_freq = [0] * len(alphabet_list)

    for letter in inputString:
        alphabet_list_freq[alphabet_list.index(letter)] += 1

    # Check if its ordered
    import copy
    alphabet_list_freq_sorted = alphabet_list_freq.copy()
    alphabet_list_freq_sorted.sort(reverse = True)

    return alphabet_list_freq == alphabet_list_freq_sorted