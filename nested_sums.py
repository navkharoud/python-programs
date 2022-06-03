def nested_sum(t):
    total = 0
    for x in t:
        total += sum(x)
    return total

def test_nested_sum():
    t=[[1, 2], [3], [4, 5, 6]]
    assert nested_sum(t)
    

if __name__ == '__main__':
    test_nested_sum()
