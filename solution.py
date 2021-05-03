# The SOLUTION class
import numpy as np
from pyrosim import pyrosim
import constants as c
import os
import random
import time


class SOLUTION:
    def __init__(self, ID):
        self.myID = ID
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)     # Create a 3x2 matrix of weights
        self.weights = self.weights * 2 - 1     # This puts the values in [-1, 1]

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        self.command = str("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")  #TODO: 2&>1
        # print(self.command)
        os.system(self.command)

    def Wait_For_Simulation_To_End(self):
        # Read in the fitness value from the fitness file
        fitnessFileName = str("fitness" + str(self.myID) + ".txt")
        while not os.path.exists(fitnessFileName):  # This will wait for the file to actually be created
            time.sleep(0.01)

        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm " + fitnessFileName)

    def Create_World(self):
        # This will tell pyrosim where to store info
        pyrosim.Start_SDF("World.sdf")

        pyrosim.Send_Cube(name="Box", pos=[c.x + 5, c.y + 5, c.z], size=[c.length, c.width, c.height])  # Create block

        pyrosim.End()

    # Create_Robot will, predictably, create a robot
    def Create_Body(self):

        # Make the actual robot
        pyrosim.Start_URDF("body.urdf")  # Make the body
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 3], size=[1, 1, 2])  # Create Torso

        # All of this stuff here is creating the limbs of the body
        # Child position is relative to parent joint

        # Left Leg
        # Joint positions are absolute
        pyrosim.Send_Joint("Torso_LeftLeg", "Torso", "LeftLeg", "revolute",
                           "-0.5 0 2", "1 0 0")
        pyrosim.Send_Cube("LeftLeg", [0, 0, -0.5], [0.2, 0.2, 1])

        # Right Leg
        # Joint positions are absolute
        pyrosim.Send_Joint("Torso_RightLeg", "Torso", "RightLeg", "revolute",
                           "0.5 0 2", "1 0 0")
        pyrosim.Send_Cube("RightLeg", [0, 0, -0.5], [0.2, 0.2, 1])

        # Right Lower Leg
        # Joint positions relative to upstream joint
        pyrosim.Send_Joint("RightLeg_RightLowerLeg", "RightLeg", "RightLowerLeg", "revolute",
                           "0 0 -1", "1 0 0")
        pyrosim.Send_Cube("RightLowerLeg", [0, 0, -0.5], [0.2, 0.2, 1])

        # Left Lower Leg
        # Joint positions relative to upstream joint
        pyrosim.Send_Joint("LeftLeg_LeftLowerLeg", "LeftLeg", "LeftLowerLeg", "revolute",
                           "0 0 -1", "1 0 0")
        pyrosim.Send_Cube("LeftLowerLeg", [0, 0, -0.5], [0.2, 0.2, 1])

        # Throw some arms on this Larry
        # Left Arm
        # Joint positions are absolute
        pyrosim.Send_Joint("Torso_LeftArm", "Torso", "LeftArm", "revolute",
                           "-0.5 0 4", "1 1 0")
        pyrosim.Send_Cube("LeftArm", [0, 0, -0.5], [0.2, 0.2, 1])

        # # Right Arm
        # # Joint positions are absolute
        # pyrosim.Send_Joint("Torso_RightArm", "Torso", "RightArm", "revolute",
        #                    "0.5 0 4", "1 1 0")
        # pyrosim.Send_Cube("RightArm", [0, 0, -0.5], [0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        brainname = "brain" + str(self.myID) + ".nndf"       # This will make the name of the brain be brainID.nndf
        # print("Brain name:", brainname)
        # Make the Brian's brain.
        pyrosim.Start_NeuralNetwork(brainname)  # Make the neural network

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(1, "LeftLeg")
        pyrosim.Send_Sensor_Neuron(2, "RightLeg")
        pyrosim.Send_Sensor_Neuron(3, "RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(4, "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(5, "LeftArm")
        # pyrosim.Send_Sensor_Neuron(6, "RightArm")

        pyrosim.Send_Motor_Neuron(6, "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(7, "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(8, "RightLeg_RightLowerLeg")
        pyrosim.Send_Motor_Neuron(9, "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(10, "Torso_LeftArm")
        # pyrosim.Send_Motor_Neuron(12, "Torso_RightArm")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=(currentColumn+c.numSensorNeurons),
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        random_row = random.randint(0, c.numSensorNeurons-1)       # Choose a random row in self.weights
        random_column = random.randint(0, c.numMotorNeurons-1)    # Choose a random column in self.weights
        self.weights[random_row][random_column] = random.random() * 2 - 1

    def Set_ID(self, newID):
        self.myID = newID
