from base.individual import *

def create_population_kp(population_size):

    return [create_individual() for _ in range(population_size)]

def evaluate_population_min(population):

    return [individual_evaluation_min(ind) for ind in population]

