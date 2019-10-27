"""
AND - both operands must be true in order for the statement to be true
OR - at least one operand must be true in order for the statement to be true
"""

def and_operator(x):
    if x < 5 and x < 10:
        print("True")
    else:
        print("False")

def or_operator(x):
    if x < 5 or x < 4:
        print("True")
    else:
        print("False")

def main():
    and_operator(5)
    or_operator(3.0


main()

"""
1. True and (True or False) = True
2. (True and False) or (True or Not(False)) = True
3. ((False and True) or (False or Not(True))) = False
"""
