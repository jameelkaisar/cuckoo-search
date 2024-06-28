import numpy as np
import matplotlib.pyplot as plt
import random
from CuckooSearch import CuckooSearch


def generate_random_fitness_equation(dimension):
    terms = []
    num_terms = random.randint(1, 10)
    for _ in range(num_terms):
        coef = random.randint(-10, 10)
        term = f"{coef}"
        num_vars = random.randint(1, min(3, dimension))
        for var_index in random.sample(range(dimension), num_vars):
            exp = random.randint(1, 5)
            term += f" * x[{var_index}] ** {exp}"
        terms.append(term)
    equation = " + ".join(terms)
    return lambda *x: eval(equation)


dimensions = range(1, 101)
nest_fitness_values = []

for dim in dimensions:
    fitness = generate_random_fitness_equation(dim)
    cs = CuckooSearch(fitness, dimentions=dim, iterations=15, verbose=False, plot_graph=False)
    solutions = cs.run()
    best_solution = solutions[-1][1]
    nest_fitness = fitness(*best_solution)
    nest_fitness_values.append(nest_fitness)


plt.figure(figsize=(12, 6))
plt.plot(dimensions, nest_fitness_values, marker='o')
plt.title('Dimension vs Nest Fitness')
plt.xlabel('Dimension')
plt.ylabel('Nest Fitness')
plt.grid(True)
plt.show()
