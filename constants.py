import numpy as np

# Initializing variables
lentime = 1000     # Number of time steps simulation will run for

# Back leg values
backLegAmplitude = np.pi / 4
backLegFrequency = 10
backLegPhaseOffset = np.pi/4

# Front leg values
frontLegAmplitude = np.pi / 4
frontLegFrequency = 10
frontLegPhaseOffset = 0

# Initialize variables to dictate size of box
length = 1
width = 1
height = 1
#
legLength = 0.2
legWidth = 1

# Initialize position variables
# Eventually I know I need to move these into a local scope
x = 0
y = 0
z = 0.5
#
# Torso coordinates
torso_x = 0
torso_y = 0
torso_z = 1

# Back leg coordinates
# back joint x = 1
# back joint y = 0
# back joint z = 1
back_x = 0
back_y = -0.5
back_z = 0

# Front leg coordinates
# front joint x = 2
# front joint y = 0
# front joint z = 1
front_x = 0
front_y = 0.5
front_z = 0

# Number of generations
numberOfGenerations = 50

# Population size
populationSize = 10

# Yeah homie idk
numSensorNeurons = 7
numMotorNeurons = 6

motorJointRange = 1