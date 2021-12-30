# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

# Solution function, gives the largest sum of a number of consecutive k numbers in an array. 
def solution(inputArray, k):
    # Add the first set
    add_i = 0
    for i in range(k):
        add_i = add_i + inputArray[i]

    # only keep the highest value
    max_val = add_i

    # Now let's add the next one and subtract the previous one.
    for i in range(len(inputArray)-k):
        add_i = - inputArray[i] + add_i + inputArray[i+k]

        if max_val < add_i:
            max_val = add_i

    return max_val
    