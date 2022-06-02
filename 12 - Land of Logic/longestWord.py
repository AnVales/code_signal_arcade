# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

# Import
import re

def solution(text):
    # Make a list of words and return the longest one
    return(max(re.findall(r'[a-zA-Z]+', text), key=len))

    

