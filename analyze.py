import numpy
import matplotlib.pyplot as plt


backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

# Make a plot of all this
plt.plot(backLegSensorValues, label="Back Leg", linewidth=2)
plt.plot(frontLegSensorValues, label="Front Leg")

# Labels are whack
plt.ylabel("Sensor Values")
plt.xlabel("Time Step")
plt.legend()

plt.show()
