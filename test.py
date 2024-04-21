from CuckooSearch import CuckooSearch


fitness_1 = lambda x, y: 2 * x**2 + 4 * x * y + 5 * x + 6 * y + 7

cs = CuckooSearch(fitness_1, iterations=15)
solutions = cs.run()

best_solution = solutions[-1][1]
nest_fitness = fitness_1(*best_solution)

print(f"Best Solution: {best_solution}, Fitness: {nest_fitness}")


fitness_2 = lambda x, y: 2 * x**2 + 3 * y**2 + 4 * x * y + 5 * x + 6 * y + 7 # Is ~3.6 a Local Minima?

cs = CuckooSearch(fitness_2, iterations=15)
solutions = cs.run()

best_solution = solutions[-1][1]
nest_fitness = fitness_2(*best_solution)

print(f"Best Solution: {best_solution}, Fitness: {nest_fitness}")


fitness_3 = lambda x, y, z: x**2 + 4 * y * z + 3 * x + 4

cs3d = CuckooSearch(fitness_3, iterations=15, dimentions=3)
solutions = cs3d.run()

best_solution = solutions[-1][1]
nest_fitness = fitness_3(*best_solution)

print(f"Best Solution: {best_solution}, Fitness: {nest_fitness}")
