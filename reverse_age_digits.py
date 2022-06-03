def check_reverse(x,y):
    return str(x).zfill(2) == str(y).zfill(2)[::-1]
def puzzle_solver(age_difference):
    son_age = 0
    mother_age = age_difference
    count = 0
    while True:
        if check_reverse(son_age,mother_age) or check_reverse(son_age,mother_age+1):
            count = count + 1
            if count == 6:
                print('Answer ',son_age,'son age' ,mother_age , 'mother age is current age')
        if mother_age > 120:
                break

        
        son_age +=  1
        mother_age += 1
    return count

def test_puzzle_solver():
    assert puzzle_solver(36)
    

if __name__ == '__main__':
    test_puzzle_solver()
