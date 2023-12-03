import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot()
x = np.random.normal(0, 3, 500)
ax.hist(x)
ax.grid()
plt.show()
