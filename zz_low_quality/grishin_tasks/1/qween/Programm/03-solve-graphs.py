from deap import base
from deap import creator
from deap import tools

import random
import numpy

import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

import elitism
import graphs



HARD_CONSTRAINT_PENALTY = 10  

POPULATION_SIZE = 100
P_CROSSOVER = 0.9 
P_MUTATION = 0.5
MAX_GENERATIONS = 100
HALL_OF_FAME_SIZE = 5
MAX_COLORS = 3

# set the random seed:
RANDOM_SEED = 123
random.seed(RANDOM_SEED)

toolbox = base.Toolbox()

# create the graph coloring problem instance to be used:
#gcp = graphs.GraphColoringProblem(nx.petersen_graph(), HARD_CONSTRAINT_PENALTY)
"""
G = nx.Graph()
G.add_node(1)
G.add_edge(1, 2)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)

G.add_node(2)
G.add_edge(2, 3)
#G.add_edge(2, 4)
G.add_node(3)
G.add_edge(3, 4)

G.add_node(4)
gcp = graphs.GraphColoringProblem(G, HARD_CONSTRAINT_PENALTY)
"""
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)
G.add_node(10)
G.add_node(11)
G.add_edge(11, 1)
G.add_edge(11, 3)
G.add_edge(11, 8)
G.add_edge(11, 5)
G.add_edge(11, 10)
G.add_edge(2, 3)
G.add_edge(2, 9)
G.add_edge(2, 1)
G.add_edge(2, 6)
G.add_edge(9, 8)
G.add_edge(9, 4)
G.add_edge(9, 10)
G.add_edge(6, 5)
G.add_edge(6, 10)
G.add_edge(6, 7)
G.add_edge(7, 8)
G.add_edge(7, 4)
G.add_edge(7, 1)
G.add_edge(4, 5)
G.add_edge(4, 3)


gcp = graphs.GraphColoringProblem(G, HARD_CONSTRAINT_PENALTY)

#gcp = graphs.GraphColoringProblem(nx.mycielski_graph(5), HARD_CONSTRAINT_PENALTY)

# define a single objective, maximizing fitness strategy:
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# create the Individual class based on list:
creator.create("Individual", list, fitness=creator.FitnessMin)

# create an operator that randomly returns an integer in the range of participating colors:
toolbox.register("Integers", random.randint, 0, MAX_COLORS - 1)

# create the individual operator to fill up an Individual instance:
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.Integers, len(gcp))

# create the population operator to generate a list of individuals:
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


# fitness calculation: cost of the suggested olution
def getCost(individual):
    return gcp.getCost(individual),  # return a tuple


toolbox.register("evaluate", getCost)

# genetic operators:
toolbox.register("select", tools.selTournament, tournsize=2)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=MAX_COLORS - 1, indpb=1.0/len(gcp))


# Genetic Algorithm flow:
def main():

    # create initial population (generation 0):
    population = toolbox.populationCreator(n=POPULATION_SIZE)

    # prepare the statistics object:
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", numpy.min)
    stats.register("avg", numpy.mean)

    # define the hall-of-fame object:
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    # perform the Genetic Algorithm flow with elitism:
    population, logbook = elitism.eaSimpleWithElitism(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,
                                              ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=True)

    # print info for best solution found:
    best = hof.items[0]
    print("-- Best Individual = ", best)
    print("-- Best Fitness = ", best.fitness.values[0])
    print()
    print("number of colors = ", gcp.getNumberOfColors(best))
    print("Number of violations = ", gcp.getViolationsCount(best))
    print("Cost = ", gcp.getCost(best))

    # plot best solution:
    plt.figure(1)
    gcp.plotGraph(best)

    # extract statistics:
    minFitnessValues, meanFitnessValues = logbook.select("min", "avg")

    # plot statistics:
    plt.figure(2)
    sns.set_style("whitegrid")
    plt.plot(minFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Min / Average Fitness')
    plt.title('Min and Average fitness over Generations')

    plt.show()


if __name__ == "__main__":
    main()
