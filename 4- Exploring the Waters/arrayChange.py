# You are given an array of integers. 
# On each move you are allowed to increase exactly one of its element by one. 
# Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

def solution(inputArray):
    prev = -float("inf")
    steps = 0

    for i in inputArray:
        if i <= prev:
            steps = steps + prev - i + 1
            prev = prev - i + i + 1
        else:
            prev = i
    return steps
