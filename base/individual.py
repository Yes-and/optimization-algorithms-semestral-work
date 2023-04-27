import random
from generate_problem import generate_problem

values_map = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}

def create_individual():
    solution = []
    letters = ["A", "C", "D", "E", "G", "F"]
    while len(letters) > 0:
        choice = random.choice(letters)
        # if solution[-1]=="F" and choice=="B":
        #     letters.remove("C")
        # if choice == "A": ask professor if it's after of right after
        #   letters += ["F"]

        if len(solution) > 0 and solution[-1] == "A" and choice == "F":
            continue

        solution.append(choice)
        letters.remove(choice)

        if solution[-1] == "F":
            solution.append("B")

    solution += ["H"]
    return solution


loss_matrix = generate_problem()  # pass this as argument to genetic algorithm?


def individual_evaluation_min(individual):
    indexes = [values_map[i] for i in individual]
    total_loss = 0
    for i in range(len(indexes) - 1):
        total_loss += loss_matrix[indexes[i]][indexes[i + 1]]  # question: loss of focus is cumulative and then subtracts to total or needs to be updated after every room passed? important because it's in %
    return total_loss
