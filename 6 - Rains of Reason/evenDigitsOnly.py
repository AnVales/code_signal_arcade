# Check if all digits of the given integer are even.

# Solution function
def solution(n):

    # Initialise variable
    even = True

    # Check if there is a rest between 2
    for digit in str(n):
        if  not int(digit) % 2 == 0:
            even = False

    return even