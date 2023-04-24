import random

def single_bit_mutation(individual, p_m):

    mutated_individual = []

    for bit in individual:
        if random.random() < p_m:
            bit = 1 - bit

        mutated_individual.append(bit)

    return mutated_individual