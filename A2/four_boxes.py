"""
Gurparteek Singh
PHYS-2112

"""
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_stright():
    print('+ - - - -', end=' ')

def print_down():
    print('|'+8*" ", end=' ')

#prints the +----+---- and ends with a +
def print_straightlines():
    do_twice(print_stright)
    print('+')

#prints |        |        and ends with |
def print_downlines():
    do_twice(print_down)
    print('|')

#prints top grid
def print_two_grids():
    print_straightlines()
    do_four(print_downlines)

#prints both the grids
def print_boxes():
    do_twice(print_two_grids)
    print_straightlines()

#execute function
print_boxes()
    