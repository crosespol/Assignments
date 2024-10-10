import numpy as np

# Create a 10x10 matrix with random 0s and 1s
matrix = np.random.randint(0, 2, (10, 10))

# Function to count surrounding 1s
def count_surrounding_ones(matrix, row, col):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) and (i != row or j != col):

                count += matrix[i][j]
                
    return count

# Iterate through the matrix and count surrounding ones for each cell
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        surrounding_ones = count_surrounding_ones(matrix, i, j)
        print(f"Cell ({i}, {j}): {matrix[i][j]}, Surrounding 1s: {surrounding_ones}")
        
print("\nOriginal Matrix:")
print(matrix)