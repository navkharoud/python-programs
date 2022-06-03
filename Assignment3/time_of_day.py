"""
Gurparteek Singh
PHYS-2112
Assignment 3
"""

from time import *

def num_of_days(t):
    #3600 seconds in hour 
    #24 hours in day 
    number_of_days = t // 3600 // 24 
    return str(number_of_days)+" Days have passed"
    


def current_time(t):

    hours  = t // 3600 #3600 seconds in 1 hour
    minutes = t // 60 #60 seconds in 1 minute
    seconds = t // 1 #round down

    #multiplication required 
    current_hours = hours - (hours // 24)*24 #floor since 24 hours in a day
    current_minutes = minutes - (minutes // 60)*60 
    current_seconds = seconds - (seconds // 60)*60

    #str and int for proper formatting 
    #can be removed to get it in a floating number manner
    return (str(int(current_hours))+":"+str(int(current_minutes))+":"+
    str(int(current_seconds)))


def test_time_of_day():
    t = time()
    print(current_time(t))
    print(num_of_days(t))

if __name__ == '__main__':
    test_time_of_day()


