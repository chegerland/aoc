#!/usr/bin/env python3
import numpy as np  

def main():

    # read file
    f = open("day4.txt", "r")
    #f = open("day4_test.txt", "r")

    lines = f.read().splitlines()
    matrix = np.array([[char for char in line] for line in lines])  

    # first index is down, second is right
    directions = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]

    # find the Xs
    rows, cols = matrix.shape
    total = 0

    for i in range(rows):
        for j in range(cols):

            if matrix[i][j] == 'X':

                for direction in directions:

                    if 0 <= i + 3*direction[0] < rows and 0 <= j + 3*direction[1] < cols:

                        if matrix[i + direction[0]][j + direction[1]] == 'M' and matrix[i + 2*direction[0]][j + 2*direction[1]] == 'A' and matrix[i + 3*direction[0]][j + 3*direction[1]] == 'S' :
                            total += 1                
                            #print(i, j, direction)


#    print(matrix)
    print(total)

    # find the Xs
    rows, cols = matrix.shape
    total = 0

    for i in range(1, rows-1):
        for j in range(1, cols-1):

            if matrix[i][j] == 'A':

                if (matrix[i - 1][j-1] == 'M' and matrix[i + 1][j+1] == 'S') or (matrix[i - 1][j-1] == 'S' and matrix[i + 1][j+1] == 'M'):
                    if (matrix[i - 1][j+1] == 'M' and matrix[i + 1][j-1] == 'S') or (matrix[i - 1][j+1] == 'S' and matrix[i + 1][j-1] == 'M'):
                        total += 1




#    print(matrix)
    print(total)

if __name__ == "__main__":
    main()
