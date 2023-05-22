from base.individual import *

# create a population
def create_population(population_size):

    return [create_individual() for _ in range(population_size)]

# evaluate the population
def evaluate_population(population, loss_matrix):

    return [evaluate_individual(individual, loss_matrix) for individual in population]

