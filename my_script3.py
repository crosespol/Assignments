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
rows = int(sys.argv[1])
columns = int(sys.argv[2])
generations = int(sys.argv[3])
import numpy as np


def dead_or_alive(matrix, rows, columns):
    cell_counter = 0
    for i in range(rows - 1, rows + 2):
        for j in range(columns - 1, columns + 2):
            if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) and (i != rows or j != columns):
                #En lloc d'afegir un altre condicional, si posem que ens sumi la posicio de la matriu, només ens sumara el 1 de la casella (que es el seu contingut), que ja es el que ens interessa per saber quants 1ns tenim
                cell_counter += matrix[i][j]
    return cell_counter
#This comunter will help us to count the generetions
gen = 1
while gen <= generations:
    #Boarders
    
    
    np.random.seed(123)
    matrix = np.random.choice([0, 1], size=(rows, columns))
    gen += 1
    
    dead_or_alive(matrix, rows, columns)
    
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
    
print("Do you want to continue? (Y/N)")
answer = input()
if answer.lower() == "y" or answer.lower() == "yes":
    print("%d" % generations, "more rounds")
elif answer.lower() == "n" or answer.lower() == "no":  
    print ("GAME OVER")