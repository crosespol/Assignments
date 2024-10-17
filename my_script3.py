'''
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, 
each of which is in one of two possible states, alive (i.e. 1) or dead (i.e. 0). 
Every cell interacts with its eight neighbors, which are the cells that are horizontally, 
vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1.
Any live cell with fewer than two live neighbors dies, as if by under-population.
2.
Any live cell with two or three live neighbors lives on to the next generation.
3.
Any live cell with more than three live neighbors dies, as if by overpopulation.
4.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The initial pattern constitutes the seed of the system. 
The first generation is created by applying the above rules simultaneously to every cell in 
the seed; births and deaths occur simultaneously, and the discrete moment at which 
this happens is sometimes called a tick. Each generation is a pure function of the preceding one.
The rules continue to be applied repeatedly to create further generations.
'''
# This as in the sem exerciese to import the values required for the exercise tu function
import sys
import numpy as np


def dead_or_alive(matrix, row, column):
    cell_counter = 0
    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) and (i != row or j != column):
                #En lloc d'afegir un altre condicional, si posem que ens sumi la posicio de la matriu, només ens sumara el 1 de la casella (que es el seu contingut), que ja es el que ens interessa per saber quants 1ns tenim
                cell_counter += matrix[i][j]
    return cell_counter
#This comunter will help us to count the generetions

# Es necesari definir una segona matriu amb els mateixos valors que la primera perque si no, estariem reescrivint la matriu mentres la analitzem i volem que es mantingui estatica, per tant assignarem els nous valors en la matriu2
#La segona matriu necessito que estigui buida, perque si no, mentres està reescrivint el contingut, solapa les matrius.

#print("\nOriginal Matrix:")
#print(matrix,"\n")
def load_the_game(rows, columns, generations):
    gen = 0
    np.random.seed(123)
    matrix = np.random.randint(0, 2, (rows, columns))
    #print(matrix) - Vaig haver d'imprimir aquesta i l'ultima matriu per veure que pasava a partir e la generació 29, que es quedava en un loop per sempre. Pero esta funcionant correctament, el programa acaba en "tablas"
    while gen < generations:
        #Initialize the matrix with zeros every time, otherwise we are overwritting the matrix in every loop
        #matrix2 = np.random.randint(0, 1, (10, 10)) - Tenia problemes i he mirat si s'arreglaven amb l'altre matriu. Les dos funcionen igual.
        matrix2 = np.zeros((rows, columns), dtype=int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                surrounding_ones = dead_or_alive(matrix, i, j)
                #print(f"Cell ({i}, {j}): {matrix[i][j]}, Surrounding 1s: {surrounding_ones}")
                if matrix[i][j] == 0 and surrounding_ones == 3:
                    matrix2[i][j] = 1
                elif matrix[i][j] == 1 and (surrounding_ones < 2 or surrounding_ones > 3):
                    matrix2[i][j] = 0
                elif matrix[i][j] == 1 and (surrounding_ones == 3 or surrounding_ones == 2):
                    matrix2[i][j] = 1
    
        gen += 1
        matrix = matrix2
        #print(matrix)
    if gen == generations:
        print("-" * (rows + 2))
        for row in matrix:
            #The borders of the box
            print("|", end='')
            for column in row:
                if column == 0:
                    print(" ", end='')
                else:
                    print("X", end='')
            #Boarders
            print("|")
    
        #Boarders
        print("-" * (rows + 2))
        #Per interpretar bé el dibuix de la matriu
        #print(matrix)
rows = int(sys.argv[1])
columns = int(sys.argv[2])
generations = int(sys.argv[3])

# He hagut de definit el joc dintre d'una funció, perquè si no no tenia manera de poder tornr-lo a cridar si l'usuaria deia que si
load_the_game(rows, columns, generations)

#Necessitava un loop per poder continuar amb el joc en el cas de resposta afirmativa

while True:
    print("Do you want to continue? (Y/N)")
    answer = input().strip().lower()
    if answer.lower() == "y" or answer.lower() == "yes":
        continues = int(input("This time, how many generations would you like to try?"))
        load_the_game(rows, columns, continues)
    elif answer.lower() == "n" or answer.lower() == "no":  
        #Game over should be printed in red.
        print ("\033[31mGAME OVER\033[0m")
        break
    else:
        print("Please enter 'Y' or 'N'.")