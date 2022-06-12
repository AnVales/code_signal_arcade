import numpy as np

# Input: value and weight
value = [2, 5, 10, 14, 15]
weight = [1, 3, 4, 5, 7]

# If it is not sorted from smallest to largest, it has to be sorted in order

# Max weight
weight_max = 8

# Initialise matrix and variable
val_matrix = np.zeros((len(value) + 1, weight_max + 1))
val_max = 0

# Complete the matrix with the values
for i in range(1, len(val_matrix)):
    for j in range(1, len(val_matrix[0])):
        
        # Fits into the backpack
        if j >= weight[i-1]:
            # New maximum value
            if val_matrix[i-1, j] <= val_matrix[i-1, j - weight[i-1]] + value[i-1]:
                val_matrix[i, j] = val_matrix[i-1, j - weight[i-1]] + value[i-1]
                val_max = val_matrix[i-1, j - weight[i-1]] + value[i-1]
            # The new total value is smaller than with previous objects
            else:
                val_matrix[i, j] = val_matrix[i-1, j]
        # New item does not fit into the backpack
        elif val_matrix[i-1, j] > 0:
            val_matrix[i, j] = val_matrix[i-1, j]


# Max value:
print(val_max)

