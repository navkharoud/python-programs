"""
Gurparteek Singh
PHYS-2112
Assignment 3
"""

def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        return False
    else:
        return True

def fermat():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose a number for c: "))
    n = int(input("Choose a number for n: "))
    return check_fermat(a, b, c, n)

def test_fermat():
    assert check_fermat(1,2,3,1)
    assert check_fermat(1,1,1,3) 
    assert check_fermat(1,1,1,1) == 1
    
if __name__ == '__main__':
    test_fermat()
