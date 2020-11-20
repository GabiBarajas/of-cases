import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
d = np.loadtxt('./postProcessing/probes/solid/0/T',comments='#')

fig, ax = plt.subplots()
ax.plot(d[:,0] , d[:,1], label='Probe 0')
ax.plot(d[:,0] , d[:,2], label='Probe 1')
ax.plot(d[:,0] , d[:,3], label='Probe 2')

ax.set(xlabel='Itteration (-)', ylabel='Temperature (K)',
       title='Temperature probe plot')
ax.grid()
ax.legend()

fig.savefig("probes.png")
plt.show()