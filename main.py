from base.individual import *
from base.population import *
from operators.selectors import *
from operators.mutators import *
from operators.crossovers import *
from algorithm.algorithm import GA

if __name__ == '__main__':

   pop, fit_pop = GA(create_population=create_population,
      evaluate_population=evaluate_population,
      maximization=False,
      gens=5,
      pop_size=10,
      selector = roulette_selection_min,
      mutator = single_bit_mutation,
      crossover_operator = one_point_crossover,
      p_c = 0.8,
      p_m = 0.2,
      elitism = True,
      verbose = True,
      log = True,
      path = 'log/test_log.csv'
      )

   print(pop, fit_pop)
