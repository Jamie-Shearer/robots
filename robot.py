import constants as c
from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os


class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.sensors = {}
        self.motors = {}
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot)        # Do I even need a comment here?
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")
        os.system("rm brain" + str(self.solutionID) + ".nndf")

    def Sense(self, t):     # Not the problem
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(t)
            # print("robot.py line 25 ------------------------------------\n", linkName)

    def Prepare_To_Sense(self):  # I hate this
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
        # print("ROBOT line 34------------", self.motors)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                self.motors[jointName].Set_Value(self.robot, desiredAngle)
                # print(neuronName, jointName, desiredAngle)
        # for jointName in self.motors:
            # self.motors[jointName].Set_Value(self.robot, t)

    def Think(self):
        # self.nn.Print()
        self.nn.Update()

    def Get_Fitness(self):
        # Get the position of the back leg
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        yPosition = basePosition[1]

        # Write the fitness value to the file
        # Right now fitness value is just how far the robot traveled to the right (We want the most negative number)
        f = open("tmp" + self.solutionID + ".txt", "w")
        f.write(str(yPosition))
        f.close()

        os.system("mv tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")
