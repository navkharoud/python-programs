"""
Gurparteek Singh
PHYS-2112
Assignment 4
"""

import math


def factorial(x):
    """
    calculates factorial for a number x using recursion
    """
    if x == 0:
        return 1
    else:
        factor = factorial(x-1)
        result = x*factor
        return result


def estimate_pi():
    total = 0 
    k = 0
    #number is the term before the summation
    number = 2*math.sqrt(2)/9801
    while True:
        num = factorial(4*k)*(1103+26390*k)
        denom = factorial(k)**4 * 396**(4*k)
        term = number * num/denom
        total += term 

        #only calculates till condition is reached for 10^-15
        if abs(term)<1e-15:
            break
        k += 1

    return 1/total    
    

def test_pi():
    assert estimate_pi() == math.pi
    #true since both are same
    assert not estimate_pi() == 3.14
    #false since decimal places are not correct
  
if __name__ == '__main__':
    test_pi()
    #print statements to test values
    #print(str(estimate_pi()))
    #print(str(math.pi))
