from base.population import *
from operators.selectors import *
from operators.mutators import *
from operators.crossovers import *
from algorithm import GA
from base.generate_problem import generate_problem, solve_problem
from itertools import product

loss_matrix = generate_problem()

param_grid = {
    "create_population": [create_population],
    "loss_matrix": [loss_matrix],
    "evaluate_population": [evaluate_population],
    "gens": [100],
    "pop_size": [20],
    "selector": [tournament_selection],
    "mutator": [reverse_sequence_mutation],
    "crossover_operator": [order_crossover],
    "p_c": [0.4],
    "p_m": [0.1],
    "elitism": [True],
    "verbose": [False],
    "log": [False],
    "path": ['log/test_log.csv'],
}


def display_results(params_list):
    headers = ["Selectors", "Mutators", "Crossovers", "P. Cross.", "P. Mut.", "Elitism"]

    # Count the occurrences of each value
    for i in range(len(headers)):
        value_count = {}
        for item in params_list:
            value = item[i]
            if value in value_count:
                value_count[value] += 1
            else:
                value_count[value] = 1
        print("-" * 10, headers[i], "-" * 10)
        for obj in sorted(value_count.items(), key=lambda x: x[1], reverse=True):
            print(obj)


if __name__ == '__main__':
    total_comb = sum(1 for _ in product(*param_grid.values()))
    lst_params, lst_fit, lst_pop, glob_found = [], [], [], 0
    iterations = 100
    avg_difference_to_global = 0

    for iteration in range(iterations):
        best_mean_fit, best_min_fit, best_params = float("+inf"), float('+inf'), None
        random.seed()
        param_grid["loss_matrix"] = [generate_problem()]
        global_optimum, global_optimum_path = solve_problem(param_grid["loss_matrix"][0])

        for count, params in enumerate(product(*param_grid.values())):
            print("Iteration #{}... {}/{}".format(iteration, count, total_comb), end="\r")
            pop, fit_pop = GA(*params)
            mean_fit = round((sum(fit_pop) / len(fit_pop)), 2)
            if mean_fit < best_mean_fit:
                best_min_fit = round(min(fit_pop), 2)
                best_mean_fit = mean_fit
                best_params = params[5:11]
                best_pop = pop
        print("Parameters: ", best_params)
        print("Mean fitness: ", best_mean_fit)
        print("Min fitness: ", best_min_fit)
        print("Global optimum: ", global_optimum)
        avg_difference_to_global += (best_min_fit - global_optimum)
        if best_min_fit == global_optimum:
            glob_found += 1
        lst_params.append(list(best_params))
        lst_fit.append(best_mean_fit)
        lst_pop.append(best_pop)

    display_results(lst_params)
    print("{}/{} iterations reached the global optimum.".format(glob_found, iterations))
    print("Average difference to global optimum: ", avg_difference_to_global/iterations)
