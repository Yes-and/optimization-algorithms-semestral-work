import random

def one_point_crossover(p1, p2):

    crossover_point = random.randint(1, len(p1))

    o1 = p1[crossover_point:] + p2[:crossover_point]
    o2 = p2[crossover_point:] + p1[:crossover_point]


    return o1, o2