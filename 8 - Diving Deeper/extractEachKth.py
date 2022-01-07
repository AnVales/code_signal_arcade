# Given array of integers, remove each kth element from it.

# Solution function
def solution(inputArray, k):
    # Return elements whose index plus one is not divisible by k
    return [inputArray[number_i] for number_i in range(len(inputArray)) if (number_i+1) % k != 0]

