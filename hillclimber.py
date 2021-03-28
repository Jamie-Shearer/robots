# Holds class HILL_CLIMBER
from solution import SOLUTION
import constants as c
import copy


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI")

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    # Spawn a copy of self.parent and name it self.child
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    # Mutate self.child
    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print("\n\n--------------------------------------------------------------------------")
        print("Parent fitness:", self.parent.fitness, "| Child fitness:", self.child.fitness)
        print("--------------------------------------------------------------------------\n\n")

    def Show_Best(self):
        self.parent.Evaluate("GUI")
