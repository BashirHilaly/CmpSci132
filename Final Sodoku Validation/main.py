"""
----------------------------------------------------
-- CMPSC_132, Spring 2024
-- Bashir Hilaly
-- Validate a 9x9 Sodoku Puzzle
----------------------------------------------------
"""
import random

samplePuzzle = [ [ 7, 8, 9, 1, 2, 3, 4, 5, 6],
            [ 4, 5, 6, 7, 8, 9, 1, 2, 3],
            [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [ 2, 3, 4, 5, 6, 7, 8, 9, 1],
            [ 5, 6, 7, 8, 9, 1, 2, 3, 4],
            [ 8, 9, 1, 2, 3, 4, 5, 6, 7],
            [ 3, 4, 5, 6, 7, 8, 9, 1, 2],
            [ 6, 7, 8, 9, 1, 2, 3, 4, 5],
            [ 9, 1, 2, 3, 4, 5, 6, 7, 8] ]

def generateRandomPuzzle():
    createdPuzzle = []

    for i in range(9):
        row = []
        for j in range(9):
            row.append(random.randrange(1, 10))
        createdPuzzle.append(row)

    # print(createdPuzzle)

    return createdPuzzle

def printPuzzle(puzzle):
    stringToPrint = ""

    for row in puzzle:
        # Where we are in the row
        pos = 0
        for number in row:
            pos += 1
            if pos != 9:
                stringToPrint += f'{number}, '
            else:
                stringToPrint += f'{number}'
        
        stringToPrint += '\n'
    
    print(stringToPrint)

if __name__ == '__main__':
    puzzle = generateRandomPuzzle()

    printPuzzle(puzzle)