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
    """
        Individual's creation
        :return: individual (list of strings)
    """
    individual = []

    # H is not here, because has it is only the last, we will append it at the end
    rooms = ["A", "B", "C", "D", "E", "F", "G"]

    # while exist rooms that were not visited:
    while rooms:

        # choose one room randomly to start
        room = random.choice(rooms)

        # if F is the room visited before the one we want to visit next, that room cannot be A
        if len(individual) != 0 and (individual[-1] == 'F' and room == 'A'):
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
            fitness_with_c = evaluate_individual(individual, loss_matrix, recursion=True)
            ind_without_C = individual[:]
            ind_without_C.remove("C")
            fitness_without_c = evaluate_individual(ind_without_C, loss_matrix, recursion=True)
            return min(fitness_with_c, fitness_without_c)
    return fitness


def fix_individual(individual):
    """
        Fixes an individual that does not respect the condition where room "A" cannot be seen right after room "F".

        If room "A" is seen after room "F" it is changed to another random index(except the same or the last).

        Args:
            individual (list): The individual to be fixed, represented as a list of room identifiers.

        Returns:
            list: The fixed individual that satisfies the condition.

    """
    fixed_individual = []
    insert_A = False

    for i in range(len(individual)):
        if individual[i] == "A" and individual[i - 1] == "F":
            insert_A = True
            continue
        fixed_individual.append(individual[i])

    if insert_A:
        fixed_individual.insert(random.choice([i for i in range(len(individual)) if individual[i] not in ['A', 'H']]),
                                "A")
    return fixed_individual


def check_validity(individual):
    for i in range(len(individual) - 1):
        if individual[i] == "F" and individual[i + 1] == "A":
            return False
    return True
