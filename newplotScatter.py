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

byarray = np.around(byarray, decimals=2)

Xa=byarray[:,[0]]
Ya=byarray[:,[1]]
Z=byarray[:,[2]]

#print(X)

fig = plt.figure()
ax = plt.axes(projection="3d")

# Uses method scatter to plot a dot plot in 3D
ax.scatter(Xa, Ya, Z, c='g', marker='o')

ax.set_xlabel('Distance')
ax.set_ylabel('Force')
ax.set_zlabel('Reaction')

plt.show()
