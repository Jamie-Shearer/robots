# The SOLUTION class
import numpy as np
from pyrosim import pyrosim
import constants as c
import os
import random


class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3, 2)     # Create a 3x2 matrix of weights
        self.weights = self.weights * 2 - 1     # This puts the values in [-1, 1]

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        self.command = str("python3 simulate.py " + directOrGUI)
        os.system(self.command)

        # Read in the fitness value from the fitness file
        f = open("fitness.txt", "r")
        self.fitness = float(f.read())
        f.close()

    def Create_World(self):
        # This will tell pyrosim where to store info
        pyrosim.Start_SDF("World.sdf")

        pyrosim.Send_Cube(name="Box", pos=[c.x + 5, c.y + 5, c.z], size=[c.length, c.width, c.height])  # Create block

        pyrosim.End()

    # Create_Robot will, predictably, create a robot
    def Create_Body(self):

        # Make the actual robot
        pyrosim.Start_URDF("body.urdf")  # Make the body
        pyrosim.Send_Cube(name="Torso", pos=[c.torso_x, c.torso_y, c.torso_z],
                          size=[c.length, c.width, c.height])  # Create Torso

        # Child position is relative to parent joint
        # Back leg
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position="1 0 1")
        pyrosim.Send_Cube("BackLeg", [c.back_x, c.back_y, c.back_z], [c.length, c.width, c.height])  # Create Leg

        # Front Leg
        pyrosim.Send_Joint("Torso_FrontLeg", "Torso", "FrontLeg", "revolute",
                           "2 0 1")
        pyrosim.Send_Cube("FrontLeg", [c.front_x, c.front_y, c.front_z], [c.length, c.width, c.height])  # Create Leg

        pyrosim.End()

    def Create_Brain(self):
        # Make the Brian.
        pyrosim.Start_NeuralNetwork("brain.nndf")  # Make the body

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(1, "BackLeg")
        pyrosim.Send_Sensor_Neuron(2, "FrontLeg")

        pyrosim.Send_Motor_Neuron(3, "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(4, "Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=(currentColumn+3),
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        random_row = random.randint(0, 2)       # Choose a random row in self.weights
        random_column = random.randint(0, 1)    # Choose a random column in self.weights
        self.weights[random_row][random_column] = random.random() * 2 - 1
