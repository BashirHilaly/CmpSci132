"""
----------------------------------------------------
-- CMPSC_132, Spring 2024
-- Lab: Calculate the Quadratic Formula
----------------------------------------------------
"""
import math

def calQuadFormula(a, b, c, whichFormula):
    # Handling division by zero or negative sqrt
    if a == 0 or (b*b - 4*a*c) < 0:
        return 0.0
    # This determines the sign (whether it is negative or positive) TRUE is Positive FALSE is Negative
    sign = 1
    if not whichFormula:
        sign = sign * -1

    answer = (-b + sign*(math.sqrt(b*b - 4*a*c)))/2*a

    return answer
        



if __name__ == "__main__":
    print("Input your 3 values for the quadratic formula in the order: a, b, c")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    # Display input values
    print(f"You're input values were as follows:\na = {a}\nb = {b}\nc = {c}\n You're two return values are:")
    print(calQuadFormula(a, b, c, True))
    print(calQuadFormula(a, b, c, False))