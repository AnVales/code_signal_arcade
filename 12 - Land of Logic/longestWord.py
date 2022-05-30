# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

text = "You are the best!!!!!!!!!!!! CodeFighter EVER[[[[[[!"
# Import
import re

def solution(text):
    # Make a list of words and return the longest one
    return(max(re.findall(r'\w+', text), key=len))

print(solution(text))
