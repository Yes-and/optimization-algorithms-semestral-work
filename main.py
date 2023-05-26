from base.population import *
from operators.selectors import *
from operators.mutators import *
from operators.crossovers import *
from algorithm.algorithm import GA
from base.generate_problem import generate_problem


loss_matrix = generate_problem()

if __name__ == '__main__':
    pop, fit_pop = GA(create_population=create_population,
                      loss_matrix=loss_matrix,
                      evaluate_population=evaluate_population,
                      gens=10000,
                      pop_size=10,
                      selector=tournament_selection,
                      mutator=reverse_sequence_mutation,
                      crossover_operator=order_crossover,
                      p_c=0.4,
                      p_m=0.1,
                      elitism=True,
                      verbose=True,
                      log=True,
                      path='log/test_log.csv'
                      )

    min_fitness_index = min(range(len(fit_pop)), key=fit_pop.__getitem__)
    print("Route: ", pop[min_fitness_index])
    print("Fitness: ", fit_pop[min_fitness_index])
