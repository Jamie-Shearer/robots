# Holds class HILL_CLIMBER
from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # These will delete all temporary files that may have been left from a previous run
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")

        self.parents = {}       # Initialize parents dictionary
        self.nextAvailableID = 0        # The ID that will be appended to brain, fitness file names
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    # Spawn a copy of self.parent and name it self.child
    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    # Mutate self.child
    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        print("\n\n")
        for key in self.parents:
            # print("\n\n--------------------------------------------------------------------------")
            print("Parent fitness:", self.parents[key].fitness, "| Child fitness:", self.children[key].fitness)
            # print("--------------------------------------------------------------------------\n\n")
        print("\n\n")

    def Show_Best(self):
        lowest = self.parents[0].fitness        # Initialize this to find the lowest fitness of the parents
        fittest = self.parents[0]
        for parent in self.parents:
            if self.parents[parent].fitness < lowest:
                lowest = self.parents[parent].fitness
                fittest = self.parents[parent]

        # Here's a little thing because I don't wanna have to watch the whole thing.
        showme = input("Show the best one? (y/n)\n")
        if showme.lower() == "n":
            exit()
        else:
            fittest.Start_Simulation("GUI")
        print("\n\n-----------------------------------------------")
        print("Best fitness:", lowest)
        print("-----------------------------------------------\n\n")

    def Evaluate(self, solutions):
        for solution in solutions:     # Run all the simulations
            # self.parents[parent].Evaluate("GUI")
            solutions[solution].Start_Simulation("GUI")     # TODO: DIRECT!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        for solution in solutions:     # Collect the fitness values
            solutions[solution].Wait_For_Simulation_To_End()
            # print("-------------------------------------------------------Fitness:", solutions[solution].fitness)
