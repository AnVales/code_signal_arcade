# CodeMaster has just returned from shopping. 
# He scanned the check of the items he bought 
# and gave the resulting string to Ratiorg to figure out the total number of purchased items. 
# Since Ratiorg is a bot he is definitely going to automate it, 
# so he needs a program that sums up all the numbers which appear in the given input.

# Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.
import re 

def solution(inputstring):
    numbers = re.findall(r'[0-9]+', inputstring)

    # Addition function: add all the values of the array
    def addition(arr): 
        # Initialize 
        sum=0

        # iterate through the array and add all the numbers
        for i in arr:
            sum = sum + int(i)
            
        return(sum) 

    return(addition(numbers))   