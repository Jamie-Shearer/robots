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

    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=50
        )
