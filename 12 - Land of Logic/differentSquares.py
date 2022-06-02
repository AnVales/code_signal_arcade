# Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

def solution(matrix):
    # Initialize 
    dic = {}
    sum = 0

    # If there are at least 2 rows and 2 columns we can have 2*2 submatrixes
    if not len(matrix)<2 or len(matrix[0])<2:

        # Loops through every position that has at least one number to its right and one number below it, 
        # stores them in a key of the dictionary if they do not exist before and adds one.
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i+1<len(matrix) and j+1<len(matrix[0]):
                    new_key = str(matrix[i][j]), str(matrix[i][j+1]), str(matrix[i+1][j]), str(matrix[i+1][j+1])
                    if not new_key in dic:
                        dic[new_key] = True
                        sum = sum + 1

    return(sum)
