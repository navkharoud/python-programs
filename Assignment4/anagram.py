"""
Gurparteek Singh
PHYS-2112
Assignment 4
"""

def is_anagram(x ,y ):
    """
    tests if the strings or lists are anagram of each other
    """
    return sorted(x)==sorted(y)



def test_anagram():
    assert is_anagram("bob","obb")
    assert is_anagram("abc","cba")
    assert not is_anagram("Singh","gurparteek") #false

  
if __name__ == '__main__':
    test_anagram()
