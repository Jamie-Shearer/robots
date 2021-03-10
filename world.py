import pybullet as p
import pybullet_data


class WORLD:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)  # Creates a physicsClient object, draws result to GUI
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Make sure we can find plane.urdf
        p.loadSDF("World.sdf")                  # Load in the file created by generate.py
        self.planeId = p.loadURDF("plane.urdf")

