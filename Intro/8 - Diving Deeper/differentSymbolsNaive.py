# Given a string, find the number of different characters in it.

# Solution function
def solution(s):

    # Initialise variable
    used_letters = []

    # Finding the letters without repeating
    [used_letters.append(letter) for letter in list(s) if letter not in used_letters]

    return len(used_letters)

