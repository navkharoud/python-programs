"""
Gurparteek Singh
PHYS-2112
Assignment 4
"""


def is_palindrome(x):
    return (x == x[::-1])

def test_palindrome2():
    assert is_palindrome("bob")
    #true since bob is a palindrome
    assert not is_palindrome("abc") 
    #False since this is not a palindrome
  
if __name__ == '__main__':
    test_palindrome2()
