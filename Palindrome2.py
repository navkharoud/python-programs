

def is_palindrome(word):
    reverse=word[::-1]
    return reverse


def test_palindrome():
    assert not is_palindrome('jaskirat') #false
    assert is_palindrome('tat')       #true
    assert not is_palindrome('mostly')   #false

if __name__ == '__main__':
    test_palindrome()