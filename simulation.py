from world import WORLD
from robot import ROBOT
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import random
import constants as c


class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        # Create environment
        p.setGravity(0, 0, -9.8)

    def Run(self):
        for i in range(c.lentime):  # Moves time forward in the physics engine by a small amount
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(self.robot, i)
            time.sleep(1/240)

    def __del__(self):
        p.disconnect()  # Closes physicsClient
