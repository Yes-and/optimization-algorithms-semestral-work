from base.individual import *
from base.population import *
from base.ks_data import *
from operators.selectors import *
from operators.mutators import *
from operators.crossovers import *
from algorithm.algorithm import GA

if __name__ == '__main__':

    # eval_kp_850 = evaluate_population_kp(850)
    #
    # GA(create_population = create_population_kp,
    #    evaluate_population = eval_kp_850,
    #    maximation= True,
    #    gens=100,
    #    pop_size=100,
    #    selector = roulette_selection_max,
    #    mutator = single_bit_mutation,
    #    crossover_operator = one_point_crossover,
    #    p_c = 0.8,
    #    p_m = 0.2,
    #    elitism = True,
    #    verbose = True,
    #    log = True,
    #    path = 'log/test_log.csv'
    #    )

   GA(create_population = create_population_kp,
      evaluate_population = evaluate_population_min,
      maximization= False,
      gens=100,
      pop_size=100,
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

