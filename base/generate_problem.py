import numpy as np
import random

encoder = {"A": 0,
           "B": 1,
           "C": 2,
           "D": 3,
           "E": 4,
           "F": 5,
           "G": 6,
           "H": 7}


def generate_problem(low=0, high=20, round_to=2):
    array = np.array(
        [[round(random.uniform(low, high), round_to) for _ in range(8)] for _ in range(8)])  # Generates initial array
    np.fill_diagonal(array, 0)  # Fill main diagonal with 0s
    max_loss = np.amax(array)  # Calculates max loss of focus

    if array[encoder["A"]][encoder["C"]] < max_loss:  # Condition: if A to C loss is smaller than max loss:
        array[encoder["A"]][encoder["C"]] = round(random.uniform(max_loss * 1.04, max_loss * 1.2),
                                                  round_to)  # Generate new value for A to C with 4% to 20% increase from previous max loss of focus

    array = np.tril(array) + np.triu(array.T, 1)

    return array  # Outputs numpy array