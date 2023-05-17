import random

def one_point_crossover(p1, p2):

    crossover_point = random.randint(1, len(p1))

    o1 = p1[crossover_point:] + p2[:crossover_point]
    o2 = p2[crossover_point:] + p1[:crossover_point]


    return o1, o2

def order_crossover(p1, p2):
    # select a set of elements from one parent, 
    # keep them, and fill the spaces with elements from another parent
    # while preserving their respective order
    how_many = 2
    parent_length = len(p1)
    crossover_index = random.randint(0, parent_length-how_many+1)
    # print(crossover_index)
    
    s1 = [p1[i] for i in range(crossover_index, crossover_index+how_many)]
    s2 = [p2[i] for i in range(crossover_index, crossover_index+how_many)]
    # print(s1, s2)

    u1 = [val for val in p2 if val not in s1]
    u2 = [val for val in p1 if val not in s2]
    # print(u1, u2)

    o1 = u1[:crossover_index] + s1 + u1[crossover_index:]
    o2 = u2[:crossover_index] + s2 + u2[crossover_index:]

    return o1, o2

def cycle_crossover(p1, p2):
    # select values from random positions from one parent
    # and fill the blanks with values from other parent
    # while preserving their respective order
    parent_length = len(p1)
    how_many = random.randint(1, parent_length-1)
    chosen_indexes = sorted(random.choices(population=[i for i in range(parent_length)], k=how_many))
    # print(how_many, chosen_indexes)

    s1 = [p1[i] for i in chosen_indexes]
    s2 = [p2[i] for i in chosen_indexes]

    u1 = [val for val in p2 if val not in s1]
    u2 = [val for val in p1 if val not in s2]

    o1, o2 = [], []
    for i in range(parent_length):
        if i in chosen_indexes:
            o1 += [s1.pop(0)]
            o2 += [s2.pop(0)]
        else:
            o1 += [u1.pop(0)]
            o2 += [u2.pop(0)]

    return o1, o2

def different_beginning_crossover(p1, p2):
    # only changes the starting part
    # because it can have a major impact
    # on the route taken afterwards
    how_many = random.randint(1, 2)
    print(how_many)

    s1 = p1[:how_many]
    s2 = p2[:how_many]

    u1 = [val for val in p2 if val not in s1]
    u2 = [val for val in p1 if val not in s1]

    o1 = s1 + u1
    o2 = s2 + u2

    return o1, o2

p1, p2 = ["A", "B", "C", "D", "E", "F", "G", "H"], ["G", "F", "E", "D", "C", "B", "A", "H"]
o1, o2 = different_beginning_crossover(p1, p2)
print(p1, p2)
print(o1, o2)