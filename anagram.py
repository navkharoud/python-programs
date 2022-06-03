def is_anagram(x,y):
    x=x.lower()
    y=y.lower()
    t1=sorted(x)
    t2=sorted(y)
    return t1==t2

def is_anagram():
    assert is_anagram('boom','moob')
    assert is_anagram('kirat','jas')
    

if __name__ == '__main__':
    is_anagram()