
'''-------------------------------------------------------------------------------------
--  CmpSc132, Spring 132 - Coding Challenge
--  BASHIR HILALY
--  Rewrite this python program.
--      1. Give the WHILE statement a meaningful test. YES
--      2. No BREAK statements allowed. YES
--      3. When the WHILE loop is over, print out the message "Out of the WHILE Loop". YES
--      4. Only one RETURN allowed.  It's the last statement, in the program.
--         Have the program return the value +55. YES
--      5. Allow user to quit if they type 'q' or 'Q', OR 
--         if its the 1st letter of the string. YES
--
--  Submit only the Python file, by the end of the class.
---------------------------------------------------------------------------------------'''

def division():
    loopValid = True

    print("Give me two numbers, and I'll divide them.")
    print("Enter 'q' to quit.")

    while loopValid:
        firstNumber = input('\nFirst number: ')

        if firstNumber[0] == 'q' or firstNumber[0] == 'Q':
            loopValid = False
        
        if loopValid:
            secondNumber = input('\nSecond number: ')

            if secondNumber[0] == 'q' or secondNumber[0] == 'Q':
                loopValid = False
            
            if loopValid:
                try:
                    answer = int(firstNumber) / int(secondNumber)
                except ZeroDivisionError:
                    print("You can't divide by 0!")
                except:
                    print ("The input values are not both integers.")
                else:
                    print(answer)    
    
    print('Out of the WHILE Loop')

    return 55

def main():
    division()

if __name__ == '__main__':
    main()