# Create a bunch of objects
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

# A loop that generates towers of boxes in a 6x6 grid
for k in range(6):              # Each iteration of this creates a row of towers
    for j in range(6):          # Each iteration of this creates a tower and moves position to next tower
        for i in range(10):     # Each iteration of this creates the next block and resizes
            pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])  # Create block
            z = z + 1               # Set position for next block
            # Resize next block
            length = length * 0.9
            width = width * 0.9
            height = height * 0.9

        # Set the position to start the next tower
        x = x + 1   # Move over 1
        z = 0.5     # It would work without this but it would take forever for all the blocks to fall

        # Resize so the first block of the next tower is the right size
        length = 1
        width = 1
        height = 1

    # Set the starting position of the next row of towers
    y = y + 1
    x = 0

pyrosim.End()
