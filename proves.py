import numpy as np
gen = 0
# Create a 10x10 matrix with random 0s and 1s
np.random.seed(123)
matrix = np.random.randint(0, 2, (10, 10))
#Necesito dos matrix perque si no es reescriu a mida que la va analitzant i els resultats son caotics
#La segona matriu necessito que estigui buida, perque si no, mentres està reescrivint el contingut, solapa les matrius.
print("\nOriginal Matrix:")
print(matrix,"\n")
# Function to count surrounding 1s
def count_surrounding_ones(matrix, row, col):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) and (i != row or j != col):

                count += matrix[i][j]
                
    return count

# Iterate through the matrix and count surrounding ones for each cell
while gen < 3:
    #Initialize the matrix with zeros every time, otherwise we are overwritting the matrix in every loop
    matrix2 = np.random.randint(0, 1, (10, 10))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            surrounding_ones = count_surrounding_ones(matrix, i, j)
            #print(f"Cell ({i}, {j}): {matrix[i][j]}, Surrounding 1s: {surrounding_ones}")
            if matrix[i][j] == 0 and surrounding_ones == 3:
                matrix2[i][j] = 1
            elif matrix[i][j] == 1 and (surrounding_ones < 2 or surrounding_ones > 3):
                matrix2[i][j] = 0
            elif matrix[i][j] == 1 and (surrounding_ones == 3 or surrounding_ones == 2):
                matrix2[i][j] = 1
            
    
    
    gen += 1
    print(matrix2)
    print(gen)
    matrix = matrix2
    
print("The Game of life after %d generations is:" % gen)
print(matrix)
