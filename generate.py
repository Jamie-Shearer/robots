# Create a single object
# This then puts an SDF file in the directory containing that object

import pybullet as p
import pyrosim.pyrosim as pyrosim

# This will tell pyrosim where to store info
# This world will be called box because it will contain a single box
pyrosim.Start_SDF("boxes.sdf")

# Initialize variables to dictate size of box
length = 1
width = 1
height = 1

# Initialize position variables
x = 0
y = 0
z = 0.5

# This is what makes the actual box
for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    z = z + 1
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9

pyrosim.End()
