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

    x=[]

    for i in lines: #:Strip all (), , and [] from the file
        if '#' in i:
            continue
        else:
            i=(re.sub(' +', ',',re.sub('[\t]', ' ',re.sub('[()]', '',i.rstrip(os.linesep)))))
            x.append(i)

    del x[0:skip]   #: Delete the values below the skip defined in the gui

    data = np.empty((0,4))

    for i in x:
        d=np.fromstring(i, dtype=float, sep=',')
        #print(d)
        data = np.append(data,np.array([[d[0],d[1],d[2],d[3]]]),axis=0)

    return data

# Data for plotting
f = readForces('./postProcessing/forces/0/force_0.dat',400)
m = readForces('./postProcessing/forces/0/moment_0.dat',400)

fig, ax = plt.subplots()
ax.plot(f[:,0] , f[:,2], label='Force (N) in y')
ax.plot(m[:,0] , m[:,2], label='Moment (Nm) around y')

ax.set(xlabel='Itteration (-)', ylabel='Force and Moment (-)',
       title='Force and moment plot')
ax.grid()
ax.legend()

fig.savefig("forces.png")
plt.show()