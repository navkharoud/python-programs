"""
Gurparteek Singh
PHYS-2112

"""
#prints same thing twice
def print_twice(argument):
    print(argument)
    print(argument)    

#does a function twice 
def do_twice(function, argument):
    function(argument)
    function(argument)

#calls the function twice 2 times
def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)


do_four(print, 'Gurparteek Singh')