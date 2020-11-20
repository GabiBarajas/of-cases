import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import re
import os


def readForces(fileName,skip):
    """Read forces or moment from a force file using the forces function object in openfoam"""

    f = open(fileName, "r")
    lines = f.readlines()
    f.close()

    x,time,xData,yData,zData=[],[],[],[],[]

    for i in lines: #:Strip all (), , and [] from the file
        if '#' in i:
            continue
        else:
            i=(re.sub(' +', ',',re.sub('[\t]', ' ',re.sub('[()]', '',i.rstrip(os.linesep)))))
            x.append(i)

    del x[0:skip]   #: Delete the values below the skip defined in the gui

    for i in x:
        data=np.fromstring(i, dtype=float, sep=',')
        time.append(data[0])             
        xData.append(data[1]+data[4])
        yData.append(data[2]+data[5])
        zData.append(data[3]+data[6])

    return [time,xData,yData,zData]

# Data for plotting
f = readForces('./postProcessing/forces/0/force_0.dat',100)

fig, ax = plt.subplots()
ax.plot(f[0] , f[1], label='Force (N) in x')

ax.set(xlabel='Itteration (-)', ylabel='Force (N)',
       title='Force plot')
ax.grid()
ax.legend()

fig.savefig("forces.png")
plt.show()