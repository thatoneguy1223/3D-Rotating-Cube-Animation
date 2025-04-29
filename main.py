import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def rotate(angle):
    return np.array([[math.cos(angle), -math.sin(angle), 0],
                     [math.sin(angle), math.cos(angle), 0],
                     [0, 0, 1]])

# Set up the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define vertices of the cube
vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]])

# Define edges connecting vertices
edges = [[0, 1], [1, 2], [2, 3], [3, 0],
         [4, 5], [5, 6], [6, 7], [7, 4],
         [0, 4], [1, 5], [2, 6], [3, 7]]

while True:  # Run the animation loop forever
    for angle in np.linspace(0, 2 * np.pi, 100):
        ax.cla()  # Clear the current plot
        rotated_vertices = vertices @ rotate(angle).T
        for edge in edges:
            line = rotated_vertices[edge, :]
            ax.plot(line[:, 0], line[:, 1], line[:, 2], 'b-')
        
        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        ax.set_zlim([-2, 2])
        
        plt.pause(0.05)  # Pause for smooth animation

plt.draw()
