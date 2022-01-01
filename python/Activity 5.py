import numpy as np
import matplotlib.pyplot as plt


results = np.loadtxt('heightvsvelocities_1.txt')
plt.figure(1)
plt.clf()
plt.xlabel('height (m)')
plt.ylabel('velocity (m/s)')
plt.title('Scenario 1')
plt.grid()
plt.plot(results[:, 0], results[:, 1], label='target v (m/s)')
plt.plot(results[:, 0], results[:, 2], label='actual v (m/s)')
plt.legend()
plt.show()

results = np.loadtxt('heightvsvelocities_5.txt')
plt.figure(1)
plt.clf()
plt.xlabel('height (m)')
plt.ylabel('velocity (m/s)')
plt.title('Scenario 5')
plt.grid()
plt.plot(results[:, 0], results[:, 1], label='target v (m/s)')
plt.plot(results[:, 0], results[:, 2], label='actual v (m/s)')
plt.legend()
plt.show()