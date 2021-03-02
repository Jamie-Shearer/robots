import numpy as np
import matplotlib.pyplot as plt

# Plotting sensor values
# backLegSensorValues = np.load("data/backLegSensorValues.npy")
# frontLegSensorValues = np.load("data/frontLegSensorValues.npy")

# Make a plot of all this
# plt.plot(backLegSensorValues, label="Back Leg", linewidth=2)
# plt.plot(frontLegSensorValues, label="Front Leg")

# Plotting target angles
backLegTargetAngles = np.load("data/blTargets.npy")
frontLegTargetAngles = np.load("data/flTargets.npy")
plt.plot(frontLegTargetAngles, label="Front Leg Motor Values", linewidth=5)
plt.plot(backLegTargetAngles, label="Back Leg Motor Values")

# Labels are whack
plt.ylabel("Desired Position")
plt.xlabel("Time Step")
plt.legend()

plt.show()
