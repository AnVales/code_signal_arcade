# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

# Add function
def add(num, add_i):
    return num + add_i

# Function adds the numbers 
def each_add(array, idx, k, add_i):
    add_i = add(array[idx], add_i)

    # If it has not yet added up all the numbers, keep on adding.
    if k != 0:
        add_i = each_add(array, idx - 1, k - 1, add_i)

    return add_i

# Solution function, gives the largest sum of a number of consecutive k numbers in an array. 
def solution(inputArray, k):
    max_ad = -float('inf')

    # Traverses the array from index k-1
    for idx in range(k-1, len(inputArray)):
        # The addition of each initial set
        add_i = 0
        # The addition of each final set
        add_i = each_add(inputArray, idx, k-1, add_i)
       
        # If the new addition is greater than the largest previous addition, replace
        if max_ad < add_i:
            max_ad = add_i

    return max_ad
