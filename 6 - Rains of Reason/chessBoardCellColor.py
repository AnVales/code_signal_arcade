# Given two cells on the standard chess board, determine whether they have the same color or not.

def solution(cell1, cell2):
    # Chess
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    number = ['1', '2', '3', '4', '5', '6', '7', '8']

    # Make the string input into lists
    cell1List = make_list(cell1)
    cell2List = make_list(cell2)

    # Obtain the index of the values
    sum1 = sum_index(cell1List, letter, number)
    sum2 = sum_index(cell2List, letter, number)

    # If both even: true
    if sum1 % 2 == 0 and sum2 % 2 == 0:
        return True
    elif sum1 % 2 != 0 and sum2 % 2 !=  0:
        return True
    else:
        return False

# Make the string input into lists function
def make_list(string):
    list = []
    [list.append(letter) for letter in string]
    return list

# Obtain the index of the values function
def sum_index(list, letter, number):
    sum = 0

    # Index letter
    for i in list:
        for idx,let in enumerate(letter):
            if i == let:
                sum = idx

    # Index number   
    for idx,num in enumerate(number):
        if i == num:
            sum = sum + idx

    return sum

