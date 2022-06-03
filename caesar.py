def rotate_word(word,x):
    string = ' '
    for letter in word:
        if letter.islower():
            alphabet_number = ord(letter)-ord('a')
            new_alphabet_number =(alphabet_number + x) % 26 + ord('a')
            string +=chr(new_alphabet_number)
            
        elif letter.isupper():
            alphabet_number = ord(letter)-ord('A')
            new_alphabet_number =(alphabet_number + x) % 26 + ord('A')
            string +=chr(new_alphabet_number)
            
        else:
            string +=letter

    return string
def test_palindrome():
    assert rotate_word('cheer', 7)
    assert rotate_word('melon', -5)
    assert rotate_word('jaskirat', 9)

if __name__ == '__main__':
    test_palindrome()
