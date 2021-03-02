# This will be the file that simulates the world in which our robots will run
# Just as a side note, .urdf stands for "Unified Robot Description Format"
# Seems pretty sus

import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import random

physicsClient = p.connect(p.GUI)    # Creates a physicsClient object, draws result to GUI
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Make sure we can find plane.urdf

# Create environment
p.setGravity(0, 0, -9.8)                # Obviously, sets gravity to simulate the real world
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("World.sdf")                  # Load in the file created by generate.py

pyrosim.Prepare_To_Simulate("body.urdf")        # Do I even need a comment here?

# Initializing variables
lentime = 3000     # So I only have to change one thing each time
# Back leg values
backLegAmplitude = np.pi / 4
backLegFrequency = 10
backLegPhaseOffset = np.pi/4
# Front leg values
frontLegAmplitude = np.pi / 4
frontLegFrequency = 10
frontLegPhaseOffset = 0

# Make vectors to put sensor values in
# backLegSensorValues = np.zeros(lentime)
# frontLegSensorValues = np.zeros(lentime)

# Create a vector that sets target position for motors
# Make array of angles from -pi/4 to pi/4. Varies sinusoidally
backLegTargetAngles = np.zeros(lentime)
for j in range(lentime):
    backLegTargetAngles[j] = backLegAmplitude * np.sin(backLegFrequency * j * (2 * np.pi / 1000) + backLegPhaseOffset)

frontLegTargetAngles = np.zeros(lentime)
for k in range(lentime):
    frontLegTargetAngles[k] = frontLegAmplitude * np.sin(frontLegFrequency * k * (2 * np.pi / 1000) + frontLegPhaseOffset)

# np.save("data/blTargets.npy", backLegTargetAngles)
# np.save("data/flTargets.npy", frontLegTargetAngles)
# exit()

# Keep the environment around for a bit, also walk through time
for i in range(lentime):       # Moves time forward in the physics engine by a small amount
    p.stepSimulation()       # One time step

    # Read sensor values from the legs
    # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Motor that connects the back leg and the torso
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robot,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=backLegTargetAngles[i],
        maxForce=50
    )

    # Motor that connects the front leg and the torso
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robot,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=frontLegTargetAngles[i],
        maxForce=50
    )

    time.sleep(1/240)        # Keep it around for a bit

p.disconnect()      # Closes physicsClient

# np.save("data/backLegSensorValues.npy", backLegSensorValues)
# np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
# print(backLegSensorValues)
