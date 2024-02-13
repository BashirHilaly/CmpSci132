"""
----------------------------------------------------
-- CMPSC_132, Spring 2024, Bashir Hilaly
-- Lab: Validate List
----------------------------------------------------
"""

def validateList(lst):
    # Holds our status of our list validity
    isValid = True
    # Checks list length for validation
    if not len(lst) == 9:
        isValid = False
        print("List is INVALID due to size")
    else:
        # Loops through list values and checks if any our out of range
        for i in lst:
            if i < 1 or i > 9:
                isValid = False
                print("List is INVALID because some values are not between 1 - 9")
        # Code that checks for duplicates
        for i in range(1, 10):
            # Loop through list and see how many times number appears. If more then one return invalid
            count = 0
            for n in lst:
                if i == n:
                    count += 1
            if count > 1:
                isValid = False
                print("List is INVALID because there are some duplicate values")
    if isValid:
        print("List is Valid")




if __name__ == '__main__':
    lst = [1, 12, 5, 6, 7, 8, 3, 4, 9]

    validateList(lst)