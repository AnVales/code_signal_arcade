# You found two items in a treasure chest! The first item weighs weight1 and is worth value1, 
# and the second item weighs weight2 and is worth value2. 
# What is the total maximum value of the items you can take with you, 
# assuming that your max weight capacity is maxW and you can't come back for the items later?

# Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

# Solution function
def solution(value1, weight1, value2, weight2, maxW):

    # Lists with weight and value information
    list_val = [value1, value2]
    list_we = [weight1, weight2]

    # Calculate the value according to the incoming weight
    if list_we[0] + list_we[1] <= maxW:
        return(list_val[0]+list_val[1])

    if list_we[0] <= maxW < list_we[1]:
        return(list_val[0])

    if list_we[1] <= maxW < list_we[0]:
        return(list_val[1])

    if list_we[0] < maxW and list_we[1] < maxW:
        return(max(list_val))
