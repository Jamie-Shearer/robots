from world import WORLD
from robot import ROBOT
import pybullet as p
import time
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
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(1/240)

    def __del__(self):
        p.disconnect()  # Closes physicsClient
