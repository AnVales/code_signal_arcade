# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

# Solution function
def solution(inputArray):

    # Initialise variables
    prev_i = inputArray[0]
    prev_dif = -float("inf")

    # Scroll through the list and subtract the elements, keeping the biggest diff
    for i in inputArray:
        if prev_i > i:
            dif  = prev_i - i
        else:
            dif  = i - prev_i
        
        if dif > prev_dif:
            prev_dif = dif
        
        prev_i = i

    return prev_dif