import numpy as np
from math import gamma
import matplotlib.pyplot as plt



class CuckooSearch():

    def __init__(self, fitness, population=100, dimentions=2, beta=1.5, pa=0.25, iterations=200, verbose=True, plot_graph=False):
        self.fitness = fitness
        self.population = population
        self.dimentions = dimentions
        self.beta = beta
        self.pa = pa
        self.iterations = iterations
        self.verbose = verbose
        self.plot_graph = plot_graph


    def generate_nests(self):
        nests = np.random.randn(self.population, self.dimentions)
        return nests


    def levy_flight(self):
        num = gamma(1 + self.beta) * np.sin(np.pi * (self.beta / 2))
        den = gamma((1 + self.beta) / 2) * self.beta * (2**((self.beta - 1) / 2))
        sgu = (num / den)**(1 / self.beta)
        sgv = 1
        u = np.random.normal(0, sgu, self.dimentions)
        v = np.random.normal(0, sgv, self.dimentions)
        S = u / (np.abs(v)**(1 / self.beta))
        return S


    def do_iter(self, nests, random_step):
        best_nest = self.get_best_nest(*nests)

        for i in range(self.population):
            value_change = np.random.randn(self.dimentions) * 0.01 * random_step * (nests[i,:] - best_nest)
            nests[i,:] = self.get_best_nest(nests[i,:], nests[i,:] + value_change)

        nests = self.abandon_nests(nests)

        return nests


    def abandon_nests(self, nests):
        nests_new = nests.copy()
        nests_result = nests.copy()

        for i in range(self.population):
            d1, d2 = np.random.randint(0, 5, 2)
            for j in range(self.dimentions):
                r = np.random.rand()
                if r < self.pa:
                    nests_new[i,j] += np.random.rand() * (nests[d1, j] - nests[d2, j]) 
            nests_result[i,:] = self.get_best_nest(nests_new[i,:], nests[i,:])

        return nests_result


    def get_fitness(self, nest):
        nest_fitness = self.fitness(*nest)
        return nest_fitness


    def get_best_nest(self, *nests):
        best_nest = min(nests, key=lambda x: np.abs(self.get_fitness(x)))
        return best_nest


    def run(self):
        nests = self.generate_nests()
        solutions = []

        if self.plot_graph:
            fitness_values = []

        for i in range(self.iterations):
            random_step = self.levy_flight()
            nests = self.do_iter(nests, random_step)
            best_nest = self.get_best_nest(*nests)
            nest_fitness = self.get_fitness(best_nest)
            solutions.append((i, best_nest))
            if self.verbose:
                print(f"Iteration: {i}, Best Nest: {best_nest}, Nest Fitness: {nest_fitness}")
            if self.plot_graph:
                fitness_values.append(nest_fitness)

        if self.plot_graph:
            plt.plot(range(self.iterations), fitness_values)
            plt.xlabel('Iteration')
            plt.ylabel('Fitness')
            plt.title('Fitness Progression')
            plt.show()

        return solutions
