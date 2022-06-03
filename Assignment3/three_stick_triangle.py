"""
Gurparteek Singh
PHYS-2112
Assignment 3
"""

def is_triangle(x, y, z):
    if z > (x+y) or y > (x+z) or x > (y+z):
        return False
    else:
        return True


def test_is_triangle():
    assert  is_triangle(1,2,3)
    assert  not is_triangle(1,2,9) #it's not possible to arrange a triangle gives error
    
if __name__ == '__main__':
    test_is_triangle()
