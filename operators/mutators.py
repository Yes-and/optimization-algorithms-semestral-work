import random


# paper used: https://arxiv.org/ftp/arxiv/papers/1203/1203.3099.pdf

def swap_mutation(individual, mutation_rate):
    """
    Apply swap mutation to an individual in a genetic algorithm.
    This mutation operator randomly swaps the positions of rooms in the individual
    based on a given mutation rate.

    :param individual: The individual to be mutated, represented as a list. (list)
    :param mutation_rate: The probability of a room being selected for mutation. (float)
    :return: The mutated individual with swapped room positions. (list)
    """
    mutated_individual = individual[:]

    for i in range(len(mutated_individual) - 1):
        if random.random() < mutation_rate:
            j = random.randint(0, len(mutated_individual) - 2)

            # Swap the positions of rooms
            mutated_individual[i], mutated_individual[j] = mutated_individual[j], mutated_individual[i]

    return mutated_individual


def reverse_sequence_mutation(individual, mutation_rate):
    """
    Applies reverse sequence mutation to an individual in a genetic algorithm.
    This mutation reverses the sequence of rooms between two random indexes.

    :param individual: The individual to be mutated. (list)
    :param mutation_rate: The probability of mutation for each individual. (float)
    :return: The mutated individual. (list)
    """

    mutated_individual = individual[:]

    if random.random() < mutation_rate:
        i = random.randint(0, len(mutated_individual) - 3)
        j = random.randint(i + 1, len(mutated_individual) - 1)

        mutated_individual[i:j] = reversed(mutated_individual[i:j])

    return mutated_individual


def partial_shuffle_mutation(individual, mutation_rate):
    """
    Applies partial shuffle mutation to an individual in a genetic algorithm.
    This mutation shuffles the sequence of rooms between two random indexes.

    :param individual: The individual to be mutated. (list)
    :param mutation_rate: The probability of mutation for each individual. (float)
    :return: The mutated individual. (list)
    """

    mutated_individual = individual[:]

    if random.random() < mutation_rate:
        i = random.randint(0, len(mutated_individual) - 3)
        j = random.randint(i + 1, len(mutated_individual) - 1)

        segment = mutated_individual[i:j]
        random.shuffle(segment)
        mutated_individual[i:j] = segment

    return mutated_individual


def twors_mutation(individual, mutation_rate):
    """
    The twors mutation allows the exchange of position of two genes randomly chosen

    :param individual: The individual to be mutated. (list)
    :param mutation_rate: The probability of mutation for each individual. (float)
    :return: mutated individual (list): offspring
    """

    # individual's copy
    mutated_individual = individual[:]

    if random.random() < mutation_rate:

        # random position
        i = random.randint(0, len(mutated_individual) - 2)
        j = random.randint(0, len(mutated_individual) - 2)
        # change the letters of i and j positions if they are not the same
        while j == i:
            j = random.randint(0, len(mutated_individual) - 2)

        mutated_individual[i], mutated_individual[j] = mutated_individual[j], mutated_individual[i]

    return mutated_individual


def centre_inverse_mutation(individual, mutation_rate):
    """
    The centre inverse mutation divides the individual into two sections.
    All genes in each section are copied and then
    inversely placed in the same section of a child.

    :param individual: The individual to be mutated. (list)
    :param mutation_rate: The probability of mutation for each individual. (float)
    :return: mutated individual (list): offspring
    """

    # individual's copy
    mutated_individual = individual[:]

    if random.random() < mutation_rate:
        # division point
        i = random.randint(0, len(mutated_individual) - 2)

        # invert the two parts of the individual
        mutated_individual[:i] = reversed(mutated_individual[:i])
        mutated_individual[i:-1] = reversed(mutated_individual[i:-1])

    return mutated_individual


def throas_mutation(individual, mutation_rate):
    """
    The throas mutation allows us to construct a sequence of three genes:
    the first is selected randomly and the two others are those two successors.
    Then, the last becomes the first of the sequence, the second becomes last and
    the first becomes the second in the sequence.

    :param individual: The individual to be mutated. (list)
    :param mutation_rate: The probability of mutation for each individual. (float)
    :return: mutated individual (list): offspring
    """

    # individual's copy
    mutated_individual = individual[:]

    if random.random() < mutation_rate:
        # selection of the three genes
        i = random.randint(0, len(mutated_individual) - 4)
        j = i + 1
        l = j + 1

        # changes between the genes
        mutated_individual[i] = individual[l]
        mutated_individual[l] = individual[j]
        mutated_individual[j] = individual[i]

    return mutated_individual


def modification_thrors_mutation(individual, mutation_rate):
    """
    The thrors mutation is very similar to throas mutation, so we modify it a little.
    The thors mutation also allows us to construct a sequence of three genes i,j, and l, and
    i < j < l, but they do not need to be consecutive.
    Then, we reverse the order that they will be placed:
    The first becomes the last, the second becomes first and
    the last becomes the second in the sequence.

    :param individual: The individual to be mutated. (list)
    :param mutation_rate: The probability of mutation for each individual. (float)
    :return: mutated individual (list): offspring
    """

    # individual's copy
    mutated_individual = individual[:]

    if random.random() < mutation_rate:
        # selection of the three genes
        i = random.randint(0, len(mutated_individual) - 4)
        j = random.randint(i + 1, len(mutated_individual) - 3)
        l = random.randint(j + 1, len(mutated_individual) - 2)

        # changes between the genes
        mutated_individual[i] = individual[j]
        mutated_individual[j] = individual[l]
        mutated_individual[l] = individual[i]

    return mutated_individual
