import math
"""Numeric fuction will calculate the calculations before sigma"""
def numeric():
    num = 2 * math.sqrt(2) / 9801
    return num

"""Factorial function is used to find factorial of any number"""
def factorial(x):
    """Computes factorial of n recursively."""
    """if the value of x is 0 then it will return 1"""
    """because zero factorial is 1"""
    if x == 0:
        return 1
    else:
        """ factor is basically causing recurssion"""
        factor = factorial(x-1)
        result = x * factor
        return result

"""Calculate pi is used to find the estimate value of pi"""
def calculatePi():
    """total will all terms"""
    total = 0
    """k will help to iterate in a loop"""
    k = 0
    
    while True:
        """numenator will do upper part of calculation"""
        numenator = factorial(4*k) * (1103 + 26390*k)
        """denominator will do lower part of calculation"""
        denomenator = factorial(k)**4 * 396**(4*k)
        """term will provide one solution of equation"""
        term = numeric() * numenator / denomenator
        total += term
        
        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / total
def testPi():
    assert calculatePi()
    print(calculatePi())


if __name__ == '__main__':
    testPi()