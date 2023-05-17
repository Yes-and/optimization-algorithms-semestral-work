import random
from base.generate_problem import loss_matrix

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
            if (len(rooms) == 1):
                individual = []
                rooms = ["A", "B", "C", "D", "E", "F", "G"]
            continue

        else:
            # add the next room
            individual.append(room)
            # delete the choosen room for the list of available rooms
            rooms.remove(room)

    individual += ["H"]
    return individual

# evaluate the fitness of an individual
def evaluate_individual(individual):

    fitness = 0
    C_optional = False
    C_index = 0

    # iterate by order all rooms of the individual(path)
    for i in range(len(individual)-1): # -1 because the last one does not have next room

        # room at index i
        current_room = individual[i]
        # room right after
        to_room = individual[i + 1]

        # loss in focus from room at index i to room at index i+1
        loss_in_focus = loss_matrix[values_map[current_room]][values_map[to_room]]

        # total fitness (sum of the loss of focus from one room to the next)
        fitness += loss_in_focus

        if current_room == 'F' and to_room == 'B':
            C_optional = True

        # keep the index of C, to forward remove it from the final solution if C is optional
        if current_room == 'C':
            C_index = i

    if C_optional:

        # if C is not in the first position of the element array, it does have a from room
        # and we should remove the fitness from that 'from room' to C
        if C_index != 0:
            from_room = individual[C_index - 1]
            fitness -= loss_matrix[values_map[from_room]][values_map['C']]

        # always remove the fitness of the room next to C
        to_room = individual[C_index + 1]
        fitness -= loss_matrix[values_map['C']][values_map[to_room]]

    return fitness
