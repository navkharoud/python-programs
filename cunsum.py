def cunsum(t):
    total=0
    new_list=[]
    for x in t:
        total=total+x
        new_list.append(total)
    return new_list

def test_cunsum():
    t = [1, 2, 3]
    assert cunsum(t)
    

if __name__ == '__main__':
    test_cunsum()

