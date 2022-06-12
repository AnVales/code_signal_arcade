# Sudoku is a number-placement puzzle. 
# The objective is to fill a 9 × 9 grid with digits so that each column,
#  each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

# This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

# https://www.geeksforgeeks.org/check-if-given-sudoku-solution-is-valid-or-not/

# Are the number in range?
def isinRange(board, N):
   
  # Traverse board[][] array
  for i in range(0, N):
    for j in range(0, N):
       
      # Check if board[i][j] lies in the range
      if not 0 < board[i][j] <= 9:
        return False
       
  return True
 
# Function to check if the solution of sudoku puzzle is valid or not

def solution(board):
   
  N = 9
   
  # Check if all elements of board[][] stores value in the range[1, 9]
  if (isinRange(board, N) == False):
    return False
 
  # Stores unique value from 1 to N
  # List with 10 false
  # The index 0 is not needed, the others indicate if there is a numeric value and is set to True.
  unique = [False] * (N + 1)
 
  # Check the numbers of the rows 
  for i in range(0, N):
     
    # Initialize unique[] array to false
    for m in range(0, N + 1):
      unique[m] = False
 
    # Traverse each column of current row
    for j in range(0, N):
       
      # Stores the value of board[i][j]
      Z = board[i][j]
 
      # Check if current row stores duplicate value
      if (unique[Z] == True):
        return False
       
      unique[Z] = True
 
  # Check the numbers of the columns
  for i in range(0, N):
     
    # Initialize unique[] array to false
    for m in range(0, N + 1):
      unique[m] = False
 
    # Traverse each row of current column
    for j in range(0, N):
       
      # Stores the value of board[j][i]
      Z = board[j][i]
 
      # Check if current column stores duplicate value
      if (unique[Z] == True):
        return False
       
      unique[Z] = True
 
  # Check each block of size 3 * 3 in board[][] array
  for i in range(0, N - 2, 3):
     
    # j stores first column of each 3 * 3 block
    for j in range(0, N - 2, 3):
       
      # Initialize unique[] array to false
      for m in range(0, N + 1):
        unique[m] = False
 
      # Check current block
      for k in range(0, 3):
        for l in range(0, 3):
           
          # Stores row number of current block
          X = i + k
 
          # Stores column number of current block
          Y = j + l
 
          # Stores the value of board[X][Y]
          Z = board[X][Y]
 
          # Check if current block stores duplicate value
          if (unique[Z] == True):
            return False
           
          unique[Z] = True
           
  # If all conditions satisfied
  return True
