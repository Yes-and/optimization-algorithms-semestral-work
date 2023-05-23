import random


def roulette_selection(population, fitnesses):
    sum_of_fitnesses = sum(fitnesses)

    probabilities = [1 - fitness / sum_of_fitnesses for fitness in fitnesses]

    return random.choices(population, weights=probabilities)[0]


def tournament_selection(population, fitnesses):
    # Part 1:
    p1_indexes = random.choices(range(len(population)), k=len(population)//2)
    p1_population = [population[i] for i in p1_indexes]
    p1_fitnesses = [fitnesses[i] for i in p1_indexes]

    # Part 2:
    winner_index = min(range(len(p1_fitnesses)), key=p1_fitnesses.__getitem__)

    return p1_population[winner_index]
