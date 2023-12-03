import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

x = np.arange(0, 1, 0.001)
frequency = 7
amplitude = 1

period = 1.0 / frequency
y = amplitude * signal.square(2 * np.pi * frequency * x)

plt.plot(x, y)
plt.show()
