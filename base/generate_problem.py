import numpy as np
import random
from itertools import permutations
from base.individual import evaluate_individual

encoder = {"A": 0,
           "B": 1,
           "C": 2,
           "D": 3,
           "E": 4,
           "F": 5,
           "G": 6,
           "H": 7}


# input data
def generate_problem(low=0, high=20, round_to=2):
    """
    Creation of a matrix that generate random values, for the
    loss of focus between each room

    :param low: the lower number for loss of focus (default=0)
    :param high: the higher number for loss of focus (default=20)
    :param round_to: decimal cases to leave (default=2)
    :return: matrix of the loss of focus for going from room to room

    """

    # Generates initial array
    loss_matrix = np.array(
        [[round(random.uniform(low, high), round_to) for _ in range(8)] for _ in range(8)])

    # Fill main diagonal with 0's
    np.fill_diagonal(loss_matrix, 0)

    # Calculates max loss of focus
    max_loss = np.amax(loss_matrix)

    # Condition: from A to C -> loss(A,C) = max_loss*1.04 (at least)
    # we choose 20% as the maximum increase of loss for it does not reach too large values
    loss_matrix[encoder['A']][encoder['C']] = round(random.uniform(max_loss * 1.04, max_loss * 1.2), round_to)

    # set the lower triangle equals to the transpose of the upper triangle
    loss_matrix = np.triu(loss_matrix) + np.tril(loss_matrix.T, -1)

    return loss_matrix


def solve_problem(loss_matrix):
    """
    Finds the global optimum using a brute force approach by checking the fitness of all possible solutions.
    The function takes a loss matrix as input, It returns the best fitness value and the corresponding
    path that leads to the global optimum.

    :param loss_matrix: A matrix representing the attention loss of traversing between different rooms.
    :return: A tuple containing the best fitness value and the corresponding path leading to the global optimum. (float, list[str])
    """

    rooms = ["A", "B", "C", "D", "E", "F", "G"]
    all_paths = permutations(rooms)
    best_fitness, best_path = float("+inf"), None
    for path in list(all_paths):
        path = list(path)
        path.append("H")
        fitness = evaluate_individual(path, loss_matrix)
        if fitness < best_fitness:
            best_fitness = fitness
            best_path = path
    return round(best_fitness, 2), best_path
