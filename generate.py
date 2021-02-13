# Create a bunch of objects
# This then puts an SDF file in the directory containing that object

import pybullet as p
import pyrosim.pyrosim as pyrosim


# Initialize variables to dictate size of box
length = 1
width = 1
height = 1

# Initialize position variables
# Eventually I know I need to move these into a local scope
x = 0
y = 0
z = 0.5


# Create_World() starts an sdf fle, sends a cube to it, and ends pyrosim
# This is not the capitalization convention I would have used
def Create_World():
    # This will tell pyrosim where to store info
    pyrosim.Start_SDF("World.sdf")

    pyrosim.Send_Cube(name="Box", pos=[x+5, y+5, z], size=[length, width, height])  # Create block

    pyrosim.End()


# Create_Robot will, predictably, create a robot
def Create_Robot():
    # Torso coordinates
    torso_x = 1.5
    torso_y = 0
    torso_z = 1.5

    # Back leg coordinates
    back_joint_x = torso_x - 0.5
    back_joint_y = torso_y
    back_joint_z = torso_z - 0.5
    back_x = -0.5
    back_y = 0
    back_z = -0.5

    # Front leg coordinates
    front_joint_x = 2
    front_joint_y = 0
    front_joint_z = 1
    front_x = 0.5
    front_y = 0
    front_z = -0.5

    # Make the actual robot
    pyrosim.Start_URDF("body.urdf")     # Make the body
    pyrosim.Send_Cube(name="Torso", pos=[torso_x, torso_y, torso_z], size=[length, width, height])    # Create Torso

    # Child position is relative to parent joint
    # Back leg
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                       position="1 0 1")
    pyrosim.Send_Cube("BackLeg", [back_x, back_y, back_z], [length, width, height])  # Create Leg

    # Front Leg
    pyrosim.Send_Joint("Torso_FrontLeg", "Torso", "FrontLeg", "revolute",
                       "2 0 1")
    pyrosim.Send_Cube("FrontLeg", [front_x, front_y, front_z], [length, width, height])  # Create Leg

    pyrosim.End()


# Uncomment these if you make changes to the robot or the world
#Create_World()
Create_Robot()
