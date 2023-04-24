import random


def roulette_selection_max(population, fitnesses):

    sum_of_fitnesses = sum(fitnesses)

    probabilities = [fitness / sum_of_fitnesses for fitness in fitnesses]

    return random.choices(population, weights = probabilities)[0]


def roulette_selection_min(population, fitnesses):

    sum_of_fitnesses = sum(fitnesses)

    probabilities = [1 - fitness / sum_of_fitnesses for fitness in fitnesses]

    return random.choices(population, weights = probabilities)[0]