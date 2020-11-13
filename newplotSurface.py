import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

x=0
F=10
byarray = np.empty(shape=[0,3])
print("Bx=0 otherwise roller would be in movement")
while x<10:
    F=10
    while F<20:
        By = ((F * x) / 10)
        byarray = np.append(byarray, [[x, F, By]], axis=0)
        F += .4
    x += .4

#byarray = np.around(byarray, decimals=2)

Xa=byarray[:,[0]]
Ya=byarray[:,[1]]
Z=byarray[:,[2]]

#print(byarray[0:20,:3])
#print(byarray[220:240,:3])

X, Y = np.meshgrid(Xa, Ya)
fig = plt.figure()
ax = plt.axes(projection="3d")

ax.plot_surface(X, Y, Z, rstride=1000, cstride=1000)

ax.set_xlabel('Distance')
ax.set_ylabel('Force')
ax.set_zlabel('Reaction')

plt.show()
