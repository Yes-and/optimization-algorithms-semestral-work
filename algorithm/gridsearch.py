from base.population import *
from operators.selectors import *
from operators.mutators import *
from operators.crossovers import *
from algorithm import GA
from base.generate_problem import generate_problem
from itertools import product

loss_matrix = generate_problem()

param_grid = {
    "create_population": [create_population],
    "loss_matrix": [loss_matrix],
    "evaluate_population": [evaluate_population],
    "gens": [100],
    "pop_size": [10],
    "selector": [roulette_selection, tournament_selection],
    "mutator": [swap_mutation, reverse_sequence_mutation, partial_shuffle_mutation, twors_mutation,
                centre_inverse_mutation, throas_mutation, modification_thrors_mutation],
    "crossover_operator": [order_crossover, cycle_crossover, partially_mapped_crossover],
    "p_c": [0.2, 0.4, 0.6, 0.8],
    "p_m": [0.1, 0.2, 0.3, 0.5],
    "elitism": [True, False],
    "verbose": [False],
    "log": [False],
    "path": ['log/test_log.csv'],
}


total_comb = sum(1 for _ in product(*param_grid.values()))
best_fit = float("+inf")

for count, params in enumerate(product(*param_grid.values())):
    print("Iterating... {}/{}".format(count, total_comb), end="\r")
    pop, fit_pop = GA(*params)
    mean_fit = round((sum(fit_pop) / len(fit_pop)), 2)
    if mean_fit < best_fit:
        best_fit = mean_fit
        best_params = params[5:11]

print(best_params)
print(best_fit)
