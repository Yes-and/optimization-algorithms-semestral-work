import random

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


# create an individual
def create_individual():
    individual = []

    # available rooms
    # H is not here, because has it is only the last, we will append it at the end
    rooms = ["A", "B", "C", "D", "E", "F", "G"]

    # while exist rooms that were not visit, do:
    while rooms:

        # choose one room randomly to start
        room = random.choice(rooms)

        # append the first room (no restrictions)
        if len(individual) == 0:
            individual.append(room)
            rooms.remove(room)

        # if F is the room visited before the one we want to visit next, that room cannot be A
        elif individual[-1] == 'F' and room == 'A':
            if len(rooms) == 1:
                individual = []
                rooms = ["A", "B", "C", "D", "E", "F", "G"]
            continue

        else:
            # add the next room
            individual.append(room)
            # delete the chosen room for the list of available rooms
            rooms.remove(room)

    individual += ["H"]
    return individual


def evaluate_individual(individual, loss_matrix, recursion=False):
    indexes = [values_map[i] for i in individual]
    fitness = 0
    for i in range(len(indexes) - 1):
        fitness += loss_matrix[indexes[i]][indexes[i + 1]]
        if individual[i] == "F" and individual[i + 1] == "B" and not recursion:
            test = individual[:]
            fitness_with_c = evaluate_individual(test, loss_matrix, recursion=True)
            test.remove("C")
            fitness_without_c = evaluate_individual(test, loss_matrix, recursion=True)
            return min(fitness_with_c, fitness_without_c)
    return fitness


# I think its better to rerun or skip mutation/crossover if the individual isnt valid, and maybe remove the restrictions in the creation of the individual

def fix_individual(individual):
    fixed_individual = []
    insert_A = False
    c_present = len(individual) == 8

    for i in range(len(individual)):
        if not c_present:
            if individual[i] == "F":
                fixed_individual += ["F", "B"]
                continue
            elif individual[i] == "B":
                continue

        else:
            if individual[i] == "A" and individual[i - 1] == "F":
                insert_A = True
                continue

        fixed_individual.append(individual[i])

    if insert_A:
        fixed_individual.insert(random.choice([i for i in range(len(individual)) if individual[i] not in ['A', 'H']]),
                                "A")

    return fixed_individual


def check_validity(individual):
    c_present = len(individual) == 8

    for i in range(len(individual) - 1):
        if not c_present:
            if individual[i] == "F" and individual[i + 1] != "B":
                return False
        else:
            if individual[i] == "F" and individual[i + 1] == "A":
                return False

    return True
