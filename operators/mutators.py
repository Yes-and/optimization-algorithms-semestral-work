import random

def single_bit_mutation(individual, p_m):

    mutated_individual = []
    rooms = ["A", "B", "C", "D", "E", "F", "G"]

    for room in individual:
        if random.random() < p_m:
            room = random.choice(rooms)

        mutated_individual.append(room)

    return mutated_individual