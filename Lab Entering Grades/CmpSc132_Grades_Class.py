"""
----------------------------------------------------
-- CMPSC_132, Spring 2024, Bashir Hilaly
-- Lab: Entering Grades Class Version
-- Grades File
----------------------------------------------------
"""

class CmpS132Grades():

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
    __letter_grades = []
    # Grading Scheme [ numericGradeRange, letterGrade, gradePointValue ]
    __grading_scheme = [
        [ (100, 93), 'A', 4.00 ],
        [ (92, 90), 'A-', 3.67 ],
        [ (89, 87), 'B+', 3.33 ],
        [ (86, 83), 'B', 3.00 ],
        [ (82, 80), 'B-', 2.67 ],
        [ (79, 76), 'C+', 2.33 ],
        [ (75, 70), 'C', 2.00 ],
        [ (69, 60), 'D', 1.00 ],
        [ (59, 0), 'F', 0 ]
    ]

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
                # Add grade points and letter grade
                # loop through grading scheme and check which item the grade fits in with
                for i in self.__grading_scheme:
                    gradeRange = i[0]
                    letterGrade = i[1]
                    gradePointValue = i[2]
                    if gradeInput in range(gradeRange[1], gradeRange[0]):
                        # Add grade points
                        self.__grade_points.append(gradePointValue * 3.00)
                        self.__letter_grades.append(letterGrade)
                        print(f"\nYour grade is within: {gradeRange}")
            else:
                self.__total_invalid_grades.append(gradeInput)
                # Print error message
                print("\nERROR: Grade Invalid. Please try again")
        
        # Update other private fields with new data
        # Find lowest valid grade
        currentLowest = 100
        for i in self.__total_valid_grades:
            if i < currentLowest:
                currentLowest = i
        self.__lowest_valid_grade = currentLowest
        # Find highest valid grade
        currentHighest = 0
        for i in self.__total_valid_grades:
            if i > currentHighest:
                currentHighest = i
        self.__highest_valid_grade = currentHighest



        # Average
        self.__avg_valid_grades = sum(self.__total_valid_grades)/len(self.__total_grades)
        return
    
    # ONLY FOR DEBUGGING, DELETE WHEN TURNING IN
    def getAllGrades(self):
        return self.__total_grades
    
    def GetLowestScore(self):
        return self.__lowest_valid_grade
    def GetHighestScore(self):
        return self.__highest_valid_grade
    def GetGPA(self):
        return sum(self.__grade_points)/(len(self.__total_valid_grades)*3.00)
    def GetGradePoints(self):
        return self.__grade_points

    # Return a string of the data in a readable string
    def __str__(self):
        
        totalGrades = f'Total Grades: {self.__total_grades}\n'
        totalValidGrades = f'Total Valid Grades: {self.__total_valid_grades}\n'
        totalInvalidGrades = f'Total Invalid Grades: {self.__total_invalid_grades}\n'
        lowestValidGrade = f'Lowest Valid Grade: {self.__lowest_valid_grade}\n'
        highestValidGrade = f'Highest Valid Grade: {self.__highest_valid_grade}\n'
        averageValidGrades = f'Average Valid Grades: {self.__avg_valid_grades}\n'
        gradePoints = f'Grade Points: {self.__grade_points}\n'
        letterGrades = f'Letter Grade: {self.__letter_grades}\n'

        
        return ("\n-----DATA----\n"
         + totalGrades 
         + totalValidGrades 
         + totalInvalidGrades 
         + lowestValidGrade 
         + highestValidGrade 
         + averageValidGrades
         + gradePoints
         + letterGrades)
