from base.individual import *


def create_population(population_size):
    """
        Population's generation

        :param population_size: number of individuals in the population (int)
        :return: list of individuals, that forms the population (list of lists)
    """

    return [create_individual() for _ in range(population_size)]


def evaluate_population(population, loss_matrix):
    """
        Population's evaluation

        :param population: the population to be evaluated (list of lists)
        :param loss_matrix: the input matrix with the loss os focus
        :return: total fitness of the population
    """
    return [evaluate_individual(individual, loss_matrix) for individual in population]
