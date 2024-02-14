"""
----------------------------------------------------
-- CMPSC_132, Spring 2024, Bashir Hilaly
-- Lab: Entering Grades Class Version
-- Main File
----------------------------------------------------
"""

from CmpSc132_Grades_Class import CmpS132Grades 

if __name__ == '__main__':

    grades = CmpS132Grades()

    grades.EnterGrades()

    print(grades.getAllGrades())
    print(grades)