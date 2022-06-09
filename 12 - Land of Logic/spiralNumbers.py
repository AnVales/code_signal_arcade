# Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, 
# starting from top-left and in clockwise direction.

def solution(n):

    # The array with the numbers
    arr = list(range(1,n**(2)+1))

    # The new array
    import numpy as np
    mat = np.zeros((n, n))

    # Initialize variables (index)
    top = 0;
    bottom = n - 1;
    left = 0;
    right = n - 1;
 
    index = 0;

    # Spiral matrix order is maintained with the help of 4 loops – left, right, top, and bottom
    while (True):
         
        if(left > right):
            break;
 
        # Top row
        for i in range(left, right + 1):
            mat[top][i] = arr[index];
            index += 1;
        top += 1;
 
        if (top > bottom):
            break;
 
        # Right column
        for i in range(top, bottom+1):
            mat[i][right] = arr[index];
            index += 1;
        right -= 1;
 
        if (left > right):
            break;
 
        # Bottom row
        for i in range(right, left-1, -1):
            mat[bottom][i] = arr[index];
            index += 1;
        bottom -= 1;
 
        if (top > bottom):
            break;
 
        # Left column
        for i in range(bottom, top-1, -1):
            mat[i][left] = arr[index];
            index += 1;
        left += 1;

    return(mat)

