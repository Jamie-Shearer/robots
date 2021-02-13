# This will be the file that simulates the world in which our robots will run
# Just as a side note, .urdf stands for "Unified Robot Description Format"
# Seems pretty sus

import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)    # Creates a physicsClient object, draws result to GUI
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Make sure we can find plane.urdf

# Create environment
p.setGravity(0, 0, -9.8)                # Obviously, sets gravity to simulate the real world
planeId = p.loadURDF("plane.urdf")
bodyId = p.loadURDF("body.urdf")
p.loadSDF("World.sdf")                  # Load in the file created by generate.py

# Keep the environment around for a bit, also walk through time
for i in range(1000):       # Moves time forward in the physics engine by a small amount
    p.stepSimulation()      # One time step
    time.sleep(1/60)        # Keep it around for a bit

p.disconnect()      # Closes physicsClient
