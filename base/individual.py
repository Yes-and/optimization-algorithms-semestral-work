# from base.ks_data import *
import random

df = None

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
    letters = ["A", "B", "C", "D", "E", "G"]
    while len(letters) > 0:
        choice = random.choice(letters)
        # if solution[-1]=="F" and choice=="B":
        #     letters.remove("C")
        if choice == "A":
            letters += ["F"]
        solution.append(choice)
        letters.remove(choice)
    solution += ["H"]
    return solution

def individual_evaluation_min(individual):

    indexes = [values_map[i] for i in individual]
    total_loss = 0
    for i in range(len(indexes)-1):
        total_loss += df.iloc[indexes[i]][indexes[i+1]]
    return total_loss

