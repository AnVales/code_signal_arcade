# In the popular Minesweeper game you have a board with some mines 
# and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. 
# Starting off with some arrangement of mines we want to create a Minesweeper game setup.

matrix = [['true', 'false', 'false'],
          ['false', 'true', 'false'],
          ['false', 'false', 'false']]

final_dim = [len(matrix), len(matrix[0])]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):

        # Esquina izquierda arriba
        if j+1<len(matrix[0])  and i+1<len(matrix) and j-1<0 and i-1<0:
            print(matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1])

        # Techo de matriz
        if j+1<len(matrix[0])  and i+1<len(matrix) and j-1>=0 and i-1<0:
            print(matrix[i][j], matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1], matrix[i] [j+1])

        # Esquina derecha arriba
        if j+1>=len(matrix[0]) and i+1<len(matrix) and j-1>=0 and i-1<0:
            print(matrix[i][j])
        
