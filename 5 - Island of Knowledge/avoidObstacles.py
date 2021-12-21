# You are given an array of integers representing coordinates of obstacles situated on a straight line.

# Assume that you are jumping from the point with coordinate 0 to the right. 
# You are allowed only to make jumps of the same length represented by some integer.

# Find the minimal length of the jump enough to avoid all the obstacles.

def solution(inputArray):

    # A list of all the numbers from 2 to 1000
    array_1000 = list(range(2,1010))

    # Number of input numbers
    inputArray_len = len(inputArray)

    # Search for the smallest number that doesn't divide the numbers with a rest of 0
    for divider in array_1000:
        counter = 0 
        for number in inputArray:
            if not number % divider == 0:
                counter = counter + 1
            if counter == inputArray_len:
                return divider
            
