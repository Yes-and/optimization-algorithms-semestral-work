import csv
import random
from copy import deepcopy
import numpy as np
from base.individual import check_validity, fix_individual


def GA(create_population,
       loss_matrix,
       evaluate_population,
       gens,
       pop_size,
       selector,
       mutator,
       crossover_operator,
       p_c,
       p_m,
       elitism,
       verbose,
       log,
       path):
    if log and path is None:
        raise Exception('If log is True then a valid path should be provided')

    pop = create_population(population_size=pop_size)

    fit_pop = evaluate_population(pop, loss_matrix)

    for it in range(gens):

        off_pop = []

        while len(off_pop) < len(pop):

            p1, p2 = selector(pop, fit_pop), selector(pop, fit_pop)

            if random.random() < p_c:
                o1, o2 = crossover_operator(p1, p2)
            else:
                o1, o2 = deepcopy(p1), deepcopy(p2)

            o1, o2 = mutator(o1, p_m), mutator(o2, p_m)

            if not check_validity(o1):
                o1 = fix_individual(o1)
            if not check_validity(o2):
                o2 = fix_individual(o2)

            off_pop.extend([o1, o2])

        if elitism:
            off_pop[-1] = pop[np.argmin(fit_pop)]

        pop = off_pop

        fit_pop = evaluate_population(pop, loss_matrix)

        if verbose:
            print(f'     {it}       |       {min(fit_pop)}      ')
            print('-' * 32)

        if log:
            with open(path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([it, min(fit_pop)])

    return pop, fit_pop
