import pygad

import numpy as np
import solver
import matplotlib.pyplot
import imageio
import operator
import functools

def fitness_func(solution, solution_idx):
    a_star = solver.Solver(np.array([[1,3,5],[7,0,2],[4,6,8]]), np.array([[1,2,3],[4,5,6],[7,8,0]]),solution, 10000)
    a_star.solve_a_star()
    output = a_star.get_summary()
    print(a_star.get_summary())
    if output == "":
        fitness = 0
    else:
        fitness = 1/(output[0]) + 1/(output[1]) + 1/(output[2])
    return fitness



fitness_function = fitness_func

num_generations = 50
num_parents_mating = 2

sol_per_pop = 8
num_genes = 2
gene_type = [float,float]

init_range_low = -10
init_range_high = 10

parent_selection_type = "sss"
keep_parents = 1

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 0.1

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

ga_instance.plot_fitness()
#ga_instance.plot_genes()
#ga_instance.plot_result()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#prediction = numpy.sum(numpy.array(function_inputs)*solution)
#print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))