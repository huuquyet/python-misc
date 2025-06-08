import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# Define the 4D vertices of a tesseract (16 vertices)
# Each vertex is represented by (x, y, z, w) coordinates, where w is the 4th dimension
vertices = np.array([
    [-1, -1, -1, -1], [1, -1, -1, -1], [-1, 1, -1, -1], [1, 1, -1, -1],
    [-1, -1, 1, -1], [1, -1, 1, -1], [-1, 1, 1, -1], [1, 1, 1, -1],
    [-1, -1, -1, 1], [1, -1, -1, 1], [-1, 1, -1, 1], [1, 1, -1, 1],
    [-1, -1, 1, 1], [1, -1, 1, 1], [-1, 1, 1, 1], [1, 1, 1, 1]
])

# Define the edges of the tesseract (connect vertices that differ in only one coordinate)
edges = []
for i in range(len(vertices)):
    for j in range(i + 1, len(vertices)):
        if np.sum(np.abs(vertices[i] - vertices[j])) == 2:  # Differ in exactly one dimension
            edges.append((i, j))

# Function to project 4D points to 3D using a simple perspective projection
def project_4d_to_3d(points, w_dist=2.0):
    x, y, z, w = points[:, 0], points[:, 1], points[:, 2], points[:, 3]
    factor = w_dist / (w_dist - w)  # Perspective projection factor based on w
    x_proj = x * factor
    y_proj = y * factor
    z_proj = z * factor
    return np.vstack((x_proj, y_proj, z_proj)).T

# Project the 4D vertices to 3D
projected_vertices = project_4d_to_3d(vertices)

# Create a 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the edges
for edge in edges:
    ax.plot3D(
        [projected_vertices[edge[0]][0], projected_vertices[edge[1]][0]],
        [projected_vertices[edge[0]][1], projected_vertices[edge[1]][1]],
        [projected_vertices[edge[0]][2], projected_vertices[edge[1]][2]],
        'b-'
    )

# Plot the vertices
ax.scatter(projected_vertices[:, 0], projected_vertices[:, 1], projected_vertices[:, 2], color='r')

# Set plot limits for better visibility
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Add labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the title
plt.title('Tesseract (4D Hypercube) Projection in 3D')

# Show the plot
plt.show()