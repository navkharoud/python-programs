"""
Gurparteek Singh
PHYS-2112
Assignment 3
"""

def first(word):
    """Returns the first character of a string."""
    return word[0]


def last(word):
    """Returns the last character of a string."""
    return word[-1]


def middle(word):
    """Returns every character except 1st and last """
    return word[1:-1]


def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


def test_palindrome():
    assert not is_palindrome('allen') #false
    assert is_palindrome('bob')       #true
    assert not is_palindrome('Van')   #false
    assert not is_palindrome('banana')#flase

    
if __name__ == '__main__':
    test_palindrome()
