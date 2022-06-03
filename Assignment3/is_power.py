"""
Gurparteek Singh
PHYS-2112
Assignment 3
"""

def is_power(a, b):
    if a < b: 
        return False 
    if a == b:  
        return True  
    else:
        return is_power(a / b, b) 
    

def test_is_power():
    assert not is_power(1,3)    #false
    assert is_power(2,2)        #true
    assert is_power(8,2)        #true

    
if __name__ == '__main__':
    test_is_power()
