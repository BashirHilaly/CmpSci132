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
    def EnterGrades():
        gradeInput = None
        while gradeInput != "-1":
            gradeInput = int(input("\nEnter a grade: "))
            __total_grades.append(gradeInput)
            # Check if the grade is valid
            if gradeInput >= 0 and gradeInput <= 100:
                


    pass