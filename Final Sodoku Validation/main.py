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
    pos = 0
    for row in puzzle:
        validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for number in row:
            if number in validNumbers:
                validNumbers.remove(number)
        if validNumbers != []:
            return { 'Status': False, 'Reason': f'The Following Numbers Not Found: {validNumbers} in Row {pos+1}' }
        # print(validNumbers)
        pos += 1
    
    return { 'Status': True, 'Reason': None }   

def validateColumns(puzzle):
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
            return { 'Status': False, 'Reason': f'The Following Numbers Not Found: {validNumbers} in Column {pos+1}' }
        pos += 1
    
    return True

def validateSquares(puzzle):
    squares = []
    square = []

    # Looping through rows of squares (1-3)
    rowPos = -3
    for i in range(0, 3):

        # Getting squares in a specific row (1-3)
        pos = -3
        for i in range(0, 3):
            square = []
            for row in range(rowPos+3, rowPos+6):
                # print('First elements: ', puzzle[row][:3])
                square.append(puzzle[row][pos+3:pos+6])
            squares.append(square)
            pos += 3
        rowPos += 3
            # print(printPuzzle(square), '\n')

    # Validate all squares

    pos = 0
    for sqr in squares:
        # put all numbers in square into one list
        nums = []
        for row in sqr:
            for num in row:
                nums.append(num)
        validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for num in nums:
            if num in validNumbers:
                validNumbers.remove(num)
        if validNumbers != []:
            return { 'Status': False, 'Reason': f'The Following Numbers Not Found: {validNumbers} in Square {pos+1}' }
        pos += 1

    return True

def validatePuzzle(puzzle):
    isValid = True
    puzzleValid = True

    # Check if all rows are valid
    rowValid = validateRows(puzzle)

    if not rowValid['Status']:
        puzzleValid = False
        print('Invalid Row(s)')
        print('\tReason: ', rowValid['Reason'])
    else:
        print('All Rows Valid')
    
    # Check if all columns are valid
    colValid = validateColumns(puzzle)
    
    if not colValid['Status']:
        puzzleValid = False
        print('Invalid Column(s)')
        print('\tReason: ', colValid['Reason'])
    else:
        print('All Columns Valid')
    
    # Check if all squares are valid
    squaresValid = validateSquares(puzzle)

    if not squaresValid['Status']:
        puzzleValid = False
        print('Invalid Square(s)')
        print('\tReason: ', squaresValid['Reason'])
    else:
        print('All Squares Valid')
    
    return puzzleValid

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
    # puzzle = generateRandomPuzzle()
    puzzle = samplePuzzle

    printPuzzle(puzzle)

    print(validatePuzzle(puzzle))
