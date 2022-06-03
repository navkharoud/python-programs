"""
Gurparteek Singh
PHYS-2112


"""
def right_justify(s):
    length_word = len(s)
    return ' '*(70- length_word)+s

print(right_justify('monty'))
print(right_justify('Gurparteek SIngh'))