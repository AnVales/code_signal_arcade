# Let's define digit degree of some positive integer as 
# the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

# Given an integer, find its digit degree.

# Solution function
def solution(n):

    # Initialise variable
    i = 0

    # While the number has more than one digit it adds
    while n >= 10:
        n_digits = [int(d) for d in str(n)]
        n = sum(n_digits)
        i = i + 1


    return i
