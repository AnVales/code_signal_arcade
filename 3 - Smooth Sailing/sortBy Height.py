# Some people are standing in a row in a park. 
# There are trees between them which cannot be moved. 
# Your task is to rearrange the people by their heights in a non-descending order without moving the trees. 
# People can be very tall!

# Solution function
def solution(a):

    # Sort the list and eliminate the -1 values
    a_sorted = sorted(a)
    a_sorted = [i for i in a_sorted if i != -1]

    # Initialise values
    a_final = []
    counter = 0

    # Replace with the numbers that are sorted but maintains the -1 values
    for i in range(len(a)):
        if a[i] == -1:
            a_final.append(a[i])
            counter = counter - 1

        else:
            a_final.append(a_sorted[i+counter])
            
    return a_final
