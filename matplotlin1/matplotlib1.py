#pip install matplotlib --proxy http://tanulo01:Tanulo0118@172.16.0.5:8080

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 20])
ypoints = np.array([0, 20])

plt.plot(xpoints, ypoints)
plt.plot([0,0],[10,0])
plt.plot([0,10],[0,0])
plt.plot([10,10],[0,10])
plt.plot([0,10],[10,10])
plt.plot([0,5],[10,17.5])
plt.plot([5,10],[17.5,10])
plt.show()
