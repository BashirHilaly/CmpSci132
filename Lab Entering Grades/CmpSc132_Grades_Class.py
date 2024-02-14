"""
----------------------------------------------------
-- CMPSC_132, Spring 2024, Bashir Hilaly
-- Lab: Entering Grades Class Version
-- Grades File
----------------------------------------------------
"""

class CmpS132Grades():

# Private fields... I think ------
    # Total of all grades entered
    __total_grades = []
    # Total of all Valid grades entered
    __total_valid_grades = []
    # Total of all Invalid grade entered
    __total_invalid_grades = []
    # Lowest Valid Grade entered
    __lowest_valid_grade = None
    # Highest Valid Grade entered
    __highest_valid_grade = None
    # Average of all valid grades entered
    __avg_valid_grades = None
    # The Grade points for this class. Assume all grades are for a 3-credit class.
    __grade_points = []
    # The Grade Letter for this class
    __letter_grade = None

    def __init__(self):
        print("\nObject has been created")
    
    # Will only return once user enters "-1"
    def EnterGrades(self):
        gradeInput = None
        while gradeInput != -1:
            gradeInput = int(input("\nEnter a grade: "))
            # End inputs
            if gradeInput == -1:
                continue
            self.__total_grades.append(gradeInput)
            # Check if the grade is valid if so put it into __total_valid_grades
            if gradeInput >= 0 and gradeInput <= 100:
                self.__total_valid_grades.append(gradeInput)
            else:
                self.__total_invalid_grades.append(gradeInput)
                # Print error message
                print("\nERROR: Grade Invalid. Please try again")
        return
    
    # ONLY FOR DEBUGGING, DELETE WHEN TURNING IN
    def getAllGrades(self):
        return self.__total_grades

    # Return a string of the data in a readable string
    def __str__(self):
        
        totalGrades = f'Total Grades: {self.__total_grades}\n'
        totalValidGrades = f'Total Valid Grades: {self.__total_valid_grades}\n'
        totalInvalidGrades = f'Total Invalid Grades: {self.__total_invalid_grades}\n'
        lowestValidGrade = f'Lowest Valid Grade: {self.__lowest_valid_grade}\n'
        highestValidGrade = f'Highest Valid Grade: {self.__highest_valid_grade}\n'
        averageValidGrades = f'Average Valid Grades: {self.__avg_valid_grades}\n'
        gradePoints = f'Grade Points: {self.__grade_points}\n'
        letterGrade = f'Letter Grade: {self.__letter_grade}\n'

        
        return ("\n-----DATA----\n"
         + totalGrades 
         + totalValidGrades 
         + totalInvalidGrades 
         + lowestValidGrade 
         + highestValidGrade 
         + averageValidGrades
         + gradePoints
         + letterGrade)
