import random


def roulette_selection(population, fitnesses):
    """
        Selects an individual from the population using the roulette wheel selection method.

        It assigns probabilities to individuals based on their fitness scores, and then selects an
        individual randomly based on these probabilities.

        Args:
            population (list): A list of individuals in the population.
            fitnesses (list): A list of fitness scores corresponding to each individual in the population.

        Returns:
            object: The selected individual from the population.
    """
    sum_of_fitnesses = sum(fitnesses)

    probabilities = [1 - fitness / sum_of_fitnesses for fitness in fitnesses]

    return random.choices(population, weights=probabilities)[0]


def tournament_selection(population, fitnesses):
    """Performs tournament selection to choose a parent individual from a population.

    Returns the individual with the lowest fitness from a randomly selected sample of 1/2 individuals of a population.

        Args:
            population (list): A list of individuals in the population.
            fitnesses (list): A list of fitness values corresponding to each individual.

        Returns:
            object: The selected individual chosen through tournament selection.
        """

    # Part 1:
    p1_indexes = random.choices(range(len(population)), k=len(population)//2)
    # After some testing we found that k=len(population)//2) produces reliable results, so we didn't include it as a parameter in the grid search to reduce the work load
    p1_population = [population[i] for i in p1_indexes]
    p1_fitnesses = [fitnesses[i] for i in p1_indexes]

    # Part 2:
    winner_index = min(range(len(p1_fitnesses)), key=p1_fitnesses.__getitem__)

    return p1_population[winner_index]
