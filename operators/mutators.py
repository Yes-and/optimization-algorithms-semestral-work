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


def twors_mutation(individual, mutation_rate):

    # allows the exchange of position of two genes randomly chosen

    mutated_individual = individual[:]

    if random.random() < mutation_rate:
        i = random.randint(0, len(mutated_individual) - 2)

        x = True
        while x:
            j = random.randint(0, len(mutated_individual) - 2)
            if j != i: x = False

            mutated_individual[i], mutated_individual[j] = mutated_individual[j], mutated_individual[i]

    return mutated_individual


def centre_inverse_mutation(individual, mutation_rate):

    # The chromosome is divided into two sections.
    # All genes in each section are copied and then
    # inversely placed in the same section of a child.

    mutated_individual = individual[:]

    if random.random() < mutation_rate:
        i = random.randint(0, len(mutated_individual) - 2)

        mutated_individual[:i] = reversed(mutated_individual[:i])
        mutated_individual[i:-1] = reversed(mutated_individual[i:-1])

    return mutated_individual


def throas_mutation(individual, mutation_rate):

    mutated_individual = individual[:]

    if random.random() < mutation_rate:
        i = random.randint(0, len(mutated_individual) - 4)
        j = i + 1
        l = j + 1

        mutated_individual[i] = individual[l]
        mutated_individual[l] = individual[j]
        mutated_individual[j] = individual[i]

    return mutated_individual


def modification_thrors_mutation(individual, mutation_rate):
    mutated_individual = individual[:]
    #print(mutated_individual)

    # i < j < l, but they do not need to be consecutive
    # we used the thrors mutation, but since it is very similar
    # to throas mutation, we decide to reverse the order

    if random.random() < mutation_rate:
        i = random.randint(0, len(mutated_individual) - 4)
        j = random.randint(i+1, len(mutated_individual) - 3)
        l = random.randint(j+1, len(mutated_individual) - 2)
        #print(i,j,l)

        mutated_individual[i] = individual[j]
        mutated_individual[j] = individual[l]
        mutated_individual[l] = individual[i]

    return mutated_individual