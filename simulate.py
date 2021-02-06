# This will be the file that simulates the world in which our robots will run

import pybullet as p
import time

physicsClient = p.connect(p.GUI)    # Creates a physicsClient object, draws result to GUI


for i in range(2000):       # Moves time forward in the physics engine by a small amount
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()      # Closes physicsClient
