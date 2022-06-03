"""
Gurparteek Singh
PHYS-2112
Assignment 3
"""

def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

def test_gcd():
    assert gcd(436,12) == 4 #true
    assert not gcd(436,12) == 3 #false test case



    
if __name__ == '__main__':
    test_gcd()
