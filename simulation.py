from world import WORLD
from robot import ROBOT
import pybullet as p
import time
import constants as c


class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        # Create environment
        self.directOrGUI = directOrGUI
        if self.directOrGUI.upper() == "GUI":
            p.connect(p.GUI)
        else:
            p.connect(p.DIRECT)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        p.setGravity(0, 0, -9.8)

    def Run(self):
        for i in range(c.lentime):  # Moves time forward in the physics engine by a small amount
            p.stepSimulation()
            self.robot.Sense(i)
            # Just stop the robot when the torso touches the ground
            # print(self.robot.sensors["Torso"].values[i])
            if (self.robot.sensors["LeftArm"].values[i] != -1.0):       #TODO: Make this work
                break
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI.upper() == "GUI":
                time.sleep(1/240)



    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()  # Closes physicsClient
