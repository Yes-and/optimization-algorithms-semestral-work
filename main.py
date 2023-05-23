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
                      selector=roulette_selection,
                      mutator=reverse_sequence_mutation,
                      crossover_operator=order_crossover,
                      p_c=0.8,
                      p_m=0.2,
                      elitism=True,
                      verbose=True,
                      log=True,
                      path='log/test_log.csv'
                      )

    print(pop, fit_pop)
