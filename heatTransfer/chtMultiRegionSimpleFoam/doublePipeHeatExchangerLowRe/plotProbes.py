import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
d1 = np.loadtxt('./postProcessing/fluidA/Average_fluidA_outlet/0/surfaceFieldValue.dat',comments='#')
d2 = np.loadtxt('./postProcessing/fluidB/Average_fluidB_outlet/0/surfaceFieldValue.dat',comments='#')

fig, ax = plt.subplots()
ax.plot(d1[:,0] , d1[:,1], label='Tavg outlet inner')
ax.plot(d2[:,0] , d2[:,1], label='Tavg outlet outer')

ax.set(xlabel='Itteration (-)', ylabel='Temperature (K)',
       title='Temperature probe plot')
ax.grid()
ax.legend()

fig.savefig("probes.png")
plt.show()