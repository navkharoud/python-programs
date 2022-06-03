"""
Gurparteek Singh
PHYS-2112
Assignment 4
"""


def nested_sum(t):
    total = 0 
    for _ in t: 
        total += sum(_)

    return total    


def test_nested_sums():
    t = [[1,2],[3],[4,5,6]]
    assert nested_sum(t)==21 
    #true 
    assert not nested_sum(t)==20
    #false
  

if __name__ == '__main__':
    test_nested_sums()
