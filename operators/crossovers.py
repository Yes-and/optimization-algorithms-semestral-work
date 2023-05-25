import random


def order_crossover(p1, p2):
    """
            The order crossover starts with selecting a set of elements from one parent,
            that goes from the crossover_point_1 from crossover_point_2, keep them,
            and then fill the spaces with elements from another parent
            while preserving their respective order

            :param p1: one parent (list of strings)
            :param p2: other parent (list of strings)
            :return: two offsprings that results from p1 and p1 (lists of strings)
    """
    # select a set of elements from one parent,
    # keep them, and fill the spaces with elements from another parent
    # while preserving their respective order

    crossover_point_1 = random.randint(0, len(p1) - 3)
    crossover_point_2 = random.randint(crossover_point_1 + 1, len(p1) - 2)

    # values between crossover points are kept from the same parent
    s1 = [p1[i] for i in range(crossover_point_1, crossover_point_2 + 1)]
    s2 = [p2[i] for i in range(crossover_point_1, crossover_point_2 + 1)]

    # other values are inserted from the other parent, while preserving order
    u1 = [val for val in p2 if val not in s1]
    u2 = [val for val in p1 if val not in s2]

    # offspring is created
    o1 = u1[:crossover_point_1] + s1 + u1[crossover_point_1:]
    o2 = u2[:crossover_point_1] + s2 + u2[crossover_point_1:]

    return o1, o2


def cycle_crossover(p1, p2):
    """
        The cyclic_crossover find a cycle between parents and fills in the rest
        preserving the order.
        For example, if the first element of parent 1 is A,
        we keep looking, until we find A in the second parent.
        We preserve elements that are part of the cycle

        :param p1: one parent (list of strings)
        :param p2: other parent (list of strings)
        :return: two offsprings that results from p1 and p1 (lists of strings)
    """
    # find a cycle and fill in the rest
    # for example, if first element of parent 1 is A,
    # we keep looking, until we find A in the second parent
    # we preserve elements that are part of the cycle
    cycle = [False] * len(p1)

    # initial variables for the cycle loop
    index = 0
    start = p1[index]
    curr = p2[index]

    # while we don't find the starting value, the cycle continues
    while True:
        cycle[index] = True
        if curr == start:
            break
        index = p1.index(curr)
        curr = p2[index]

    # initializing empty offsrping
    o1, o2 = [], []
    for i in range(len(p1)):
        # values that are inside the cycle are preserved from the original parent
        if cycle[i] == True:
            o1.append(p1[i]), o2.append(p2[i])
        # values outside the cycle are imported from the other parent
        else:
            o1.append(p2[i]), o2.append(p1[i])

    return o1, o2


def partially_mapped_crossover(p1, p2):
    """
        The partially mapped crossover defines two different crossover points, and preserve
        the values between them form the original parents.
        The rest values are mapped using a cycle.

        :param p1: one parent (list of strings)
        :param p2: other parent (list of strings)
        :return: two offsprings that results from p1 and p2 (lists of strings)
    """
    # values between crossover points are preserved from the original parent
    # the rest of the values is mapped using a cycle
    crossover_index = 3
    how_many = 4

    # preserved values
    s1 = [p1[i] for i in range(crossover_index, crossover_index + how_many)]
    s2 = [p2[i] for i in range(crossover_index, crossover_index + how_many)]

    # remaining values
    u1 = [val for val in p2 if val not in s2]
    u2 = [val for val in p1 if val not in s1]

    # create arrays of parents for simpler looping
    un = [u1, u2]
    sn = [s1, s2]
    pn = [p1, p2]

    # cycle detection
    for i in range(len(u1)):
        for j in range(2):
            curr = un[j][i]
            while True:
                if curr in sn[j]:
                    index = pn[j].index(curr)
                    curr = pn[1 - j][index]
                else:
                    un[j][i] = curr
                    break

    # offspring is created
    o1 = u1[:crossover_index] + s1 + u1[crossover_index:]
    o2 = u2[:crossover_index] + s2 + u2[crossover_index:]

    return o1, o2


def different_beginning_crossover(p1, p2):
    # only changes the starting part
    # because it can have a major impact on the route taken afterwards
    how_many = random.randint(1, 4)

    # 1:n elements are preserved from the original parent
    s1 = p1[:how_many]
    s2 = p2[:how_many]

    # the rest is filled out with data from the other parent
    # while preserving their respectiv eorder
    u1 = [val for val in p2 if val not in s1]
    u2 = [val for val in p1 if val not in s2]

    # offspring is created
    o1 = s1 + u1
    o2 = s2 + u2

    return o1, o2
