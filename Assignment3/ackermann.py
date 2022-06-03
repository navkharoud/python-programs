"""
Gurparteek Singh
PHYS-2112
Assignment 3
"""


def ackermann(m, n):
    """Computes the Ackermann function A(m, n)
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))



def test_ackermann():
    assert ackermann(1,2) 
    #print( ackermann(1,2))
    assert ackermann(3,5) 
    #print( ackermann(3,5))
    assert not ackermann(6,7) #gives error
    

    
if __name__ == '__main__':
    test_ackermann()
