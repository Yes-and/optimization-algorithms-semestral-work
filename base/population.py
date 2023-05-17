from base.individual import *

# create a population
def create_population(population_size):

    return [create_individual() for _ in range(population_size)]

# evaluate the population
def evaluate_population(population):

    return [evaluate_individual(individual) for individual in population]

