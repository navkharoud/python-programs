"""
Gurparteek Singh
PHYS-2112
Assignment 4
"""
def are_reversed(x,y):
    """
    checks if x and y are reverse of each other, also filles them with 2 digits
    """
    return str(x).zfill(2) == str(y).zfill(2)[::-1]



def num_instances(diff):
    """Counts the number of palindromic ages.
    returns a list with combinations of both the mother and daughter's palindromic ages, Using a list because its a better option, could return a string aswell 
    """
    daughter = 0 #using daughter and mother variable since question states it, can use person1 and person2 aswell
    count = 0
    total = [] #returning list
    while True:
        mother = daughter + diff

        # assuming that mother and daughter don't have the same birthday,
        # they have two chances per year to have palindromic ages.
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            total.append((daughter, mother))
        if mother > 120:
            break
        daughter = daughter + 1
    return total
    

def reverse_age_digits(x,y):
    """
    Input takes in 2 ages and finds all the 2 digit ages that are swapped digits
    x = daughter's age
    y = mother's age
    """
    diff = y-x 
    return (num_instances(diff))




def test_reverse_age_digits():
   assert reverse_age_digits(37,73) == [(4, 40), (15, 51), (26, 62), (37, 73), (48, 84), (59, 95)]
   #true since these are all the ages 
   assert not reverse_age_digits(10,2)
   #wont run since diff becomes negative

    
  
if __name__ == '__main__':
    test_reverse_age_digits()
    #print(reverse_age_digits(37,73))
    
