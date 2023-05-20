import random

def order_crossover(p1, p2):
    # select a set of elements from one parent, 
    # keep them, and fill the spaces with elements from another parent
    # while preserving their respective order
    how_many = 2
    parent_length = len(p1)
    crossover_index = random.randint(0, parent_length-how_many)

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
    # find a cycle and fill in the rest
    cycle = [False]*len(p1)

    index = 0
    start = p1[index]
    curr = p2[index]
    while True:
        cycle[index] = True
        if curr==start:
            break
        index = p1.index(curr)
        curr = p2[index]

    o1, o2 = [], []
    for i in range(len(p1)):
        if cycle[i]==True:
            o1.append(p1[i]), o2.append(p2[i])
        else:
            o1.append(p2[i]), o2.append(p1[i])

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

p1, p2 = ["A", "B", "D", "C", "E", "F", "G", "H"], ["G", "C", "E", "D", "B", "A", "F", "H"]
o1, o2 = cycle_crossover(p1, p2)
print(p1, p2)
print(o1, o2)