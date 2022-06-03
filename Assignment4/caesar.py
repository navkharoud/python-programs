"""
Gurparteek Singh
PHYS-2112
Assignment 4
"""

def rotate_word(s = str, num = int):
    """
        rotates string s's characters by int num's places
    """
   
    #empty string for returning 
    rotated = ''
    #rotating every single character x in string s
    for x in s:

        if x.isupper():
            start = ord('A')
        elif x.islower():
            start = ord('a')
        else: 
            #case for assuming inputted string has numbers
            start = int(x)     

        c = ord(x) - start
        i = (c + num) % 26 + start
        rotated += chr(i)

    return rotated
        

def test_ceaser():
    assert rotate_word("cheer", 7) == "jolly"
    #true 
    assert not rotate_word("abc",3) == "abc"
  
if __name__ == '__main__':
    test_ceaser()
    #print(str(rotate_word("cheer3",7)))

