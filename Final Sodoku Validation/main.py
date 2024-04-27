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

def validateRows(puzzle):
    # Check if all rows are valid
    for row in puzzle:
        validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for number in row:
            if number in validNumbers:
                validNumbers.remove(number)
        if validNumbers != []:
            return False
        # print(validNumbers)
    return True
    

def validateColumns():
    # Check if all columns are valid
    pos = 0
    for i in range(9):
        validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        column = []
        for row in puzzle:
            column.append(row[pos])
        for number in column:
            if number in validNumbers:
                validNumbers.remove(number)
        if validNumbers != []:
            # Find a way to end the loop here
            return False
        pos += 1
    return True

def validateSquares(puzzle):
    squares = []
    square = []
    for row in range(0, 3):
        print('First elements: ', puzzle[row][:3])
        square.append(puzzle[row][:3])
    squares.append(square)
    
    print(printPuzzle(square))

    return square

def validatePuzzle(puzzle):
    isValid = True
    invalidMessage = ''

    # Check if all rows are valid
    isValid = validateRows(puzzle)
    invalidMessage = 'Invalid Row(s)'

    if not isValid:
        print(invalidMessage)
        return invalidMessage
    
    # Check if all columns are valid
    isValid = validateColumns(puzzle)
    invalidMessage = 'Invalid Column(s)'
    
    if not isValid:
        print(invalidMessage)
        return invalidMessage


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
            if pos != len(puzzle):
                stringToPrint += f'{number}, '
            else:
                stringToPrint += f'{number}'
        
        stringToPrint += '\n'
    
    print(stringToPrint)

if __name__ == '__main__':
    #puzzle = generateRandomPuzzle()
    puzzle = samplePuzzle

    printPuzzle(puzzle)

    print('\n')
    firstSquare = validateSquares(puzzle)
    print('First Square:', printPuzzle(firstSquare))