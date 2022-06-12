# In the popular Minesweeper game you have a board with some mines 
# and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. 
# Starting off with some arrangement of mines we want to create a Minesweeper game setup.

# Solution function
def solution(matrix):
    import numpy as np

    # Final dimensions
    final_dim = [len(matrix), len(matrix[0])]
    mines_array = []

    # Traverses the array
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            mines = 0

            # Fila anterior y columna anterior
            if i-1>=0 and j-1>=0 and matrix[i-1][j-1]:
                mines = mines + 1

            # Fila anterior y columna actual
            if i-1>=0 and matrix[i-1][j]:
                mines = mines + 1

            # Fila anterior y columna posterior
            if i-1>=0 and j+1<len(matrix[0]) and matrix[i-1][j+1]:
                mines = mines + 1

            # Fila actual y columna anterior
            if j-1>=0 and matrix[i][j-1]:
                mines = mines + 1

            # Fila actual y columna posterior
            if j+1<len(matrix[0]) and matrix[i][j+1]:
                mines = mines + 1

            # Fila siguiente y columna anterior
            if i+1<len(matrix) and j-1>=0 and matrix[i+1][j-1]:
                mines = mines + 1

            # Fila siguiente y columna actual
            if i+1<len(matrix) and matrix[i+1][j]:
                mines = mines + 1

            # Fila siguiente y columna siguiente
            if i+1<len(matrix) and j+1<len(matrix[0]) and matrix[i+1][j+1]:
                mines = mines + 1

            mines_array.append(mines)

    return(np.resize(mines_array,final_dim))