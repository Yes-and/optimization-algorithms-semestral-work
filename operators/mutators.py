import random


# paper used: https://arxiv.org/ftp/arxiv/papers/1203/1203.3099.pdf

def swap_mutation(individual, mutation_rate):
    mutated_individual = individual[:]

    for i in range(len(mutated_individual) - 1):
        if random.random() < mutation_rate:
            j = random.randint(0, len(mutated_individual) - 2)

            # Swap the positions of cities
            mutated_individual[i], mutated_individual[j] = mutated_individual[j], mutated_individual[i]

    return mutated_individual


def reverse_sequence_mutation(individual, mutation_rate):
    mutated_individual = individual[:]

    if random.random() < mutation_rate:
        i = random.randint(0, len(mutated_individual) - 3)
        j = random.randint(i + 1, len(mutated_individual) - 1)

        mutated_individual[i:j] = reversed(mutated_individual[i:j])

    return mutated_individual


def partial_shuffle_mutation(individual, mutation_rate):
    mutated_individual = individual[:]

    if random.random() < mutation_rate:
        i = random.randint(0, len(mutated_individual) - 3)
        j = random.randint(i + 1, len(mutated_individual) - 1)

        segment = mutated_individual[i:j]
        random.shuffle(segment)
        mutated_individual[i:j] = segment

    return mutated_individual
