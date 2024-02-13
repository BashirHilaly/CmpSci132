"""
----------------------------------------------------
-- CMPSC_132, Spring 2024, Bashir Hilaly
-- Lab: Frugal Calendar
----------------------------------------------------
"""

"""
Simple trick is

remainder 0 add 28 years

For remainder 1 add 6 years

For a remainder, 2&3 add 11 years
"""

def nextUsableYear(year):

    # This value will change after our calculations
    nextUsableYear = year

    if year % 4 == 1:
        nextUsableYear += 6
    elif year % 4 == 2 or year % 3:
        nextUsableYear += 11
    elif year % 4 == 0:
        nextUsableYear += 28
    
    # Return changed value
    return nextUsableYear


if __name__ == "__main__":

    # When this is true, the program ends
    stopProgram = False

    userInputYear = None

    while stopProgram == False:
        # User inputs a year
        userInputYear = int(input("Enter a year: "))

        # Checks if the year is within the bounds if not then stopProgram remains true and the while loop repeats
        if userInputYear > 1900 and userInputYear < 2022:
            # Call function and print the statement
            print(f'The {userInputYear} calendar can be used again in {nextUsableYear(userInputYear)}.')

        # to stop the program user must enter "0"
        elif userInputYear == 0:
            stopProgram = True
