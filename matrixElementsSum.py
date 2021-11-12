# After becoming famous, the CodeBots decided to move into a new building together. 
# Each of the rooms has a different cost, and some of them are free, 
# but there's a rumour that all the free rooms are haunted! 
# Since the CodeBots are quite superstitious, 
# they refuse to stay in any of the free rooms, 
# or any of the rooms below any of the free rooms.

# Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, 
# your task is to return the total sum of all rooms that are suitable for the CodeBots 
# (ie: add up all the values that don't appear below a 0).

matrix_a = [[0,1,1,2], 
            [0,5,0,0], 
            [2,0,3,3]]

matrix_b = matrix_a
value = 0

for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        if matrix_a[i][j] == 0 and i+1<len(matrix_a):
            matrix_b[i+1][j] = 0

for i in range(len(matrix_b)):
    for j in range(len(matrix_b[0])):
        value = matrix_a[i][j] + value

print(value)

