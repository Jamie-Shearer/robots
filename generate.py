# Create a single object
# This then puts an SDF file in the directory containing that object

import pybullet as p
import pyrosim.pyrosim as pyrosim

# This will tell pyrosim where to store info
# This world will be called box because it will contain a single box
pyrosim.Start_SDF("box.sdf")

# Initialize variables to dictate size of box
length = 1
width = 2
height = 3

# This is what makes the actual box
pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[length, width, height])

pyrosim.End()
