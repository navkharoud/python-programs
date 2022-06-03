"""
Gurparteek Singh
PHYS-2112
Assignment 4
"""

def cumsum(t):
    total = 0
    result = []
    for _ in t: 
        total+= _
        result.append(total)

    return result


def test_cumsum():
    t = [1,2,3]
    assert cumsum(t) == [1,3,6] 
    #print(str(cumsum(t)))
    assert not cumsum(t) == [1,2,3]
  
if __name__ == '__main__':
    test_cumsum()
