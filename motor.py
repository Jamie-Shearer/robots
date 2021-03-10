import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

        self.amplitude = c.backLegAmplitude
        self.frequency = c.backLegFrequency
        self.offset = c.backLegPhaseOffset
        self.motorValues = np.zeros(c.lentime)
        pyrosim.Prepare_To_Simulate("body.urdf")        # Do I even need a comment here?

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        # Create a vector that sets target position for motors
        # Make array of angles from -pi/4 to pi/4. Varies sinusoidally

        # I hate this
        for j in range(c.lentime):
            if self.jointName == "Torso_BackLeg":
                self.motorValues[j] = self.amplitude * np.sin(
                    self.frequency * j * (2 * np.pi / 1000) + self.offset)
            else:
                self.motorValues[j] = self.amplitude * np.sin(
                    self.frequency * j * (np.pi / 1000) + self.offset)

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=50
        )
