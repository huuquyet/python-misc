import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

φ = (1 + 5 ** 0.5) / 2           # golden ratio
min_side = 1e-3                  # stop when a square is this small
fig, ax = plt.subplots(figsize=(6, 6))

# start with two 1×1 squares
sides = [1, 1]                   # side lengths, working inward
while sides[-1] > min_side:
    sides.append(sides[-2] / φ)  # each next square is smaller by 1/φ

# draw squares and quarter-circles
x, y = 0, 0                      # lower-left corner of current square
orientation = 0                  # 0=right, 1=up, 2=left, 3=down
for side in sides:
    # square
    ax.add_patch(patches.Rectangle((x, y), side, side,
                                   edgecolor='black', facecolor='none'))
    # quarter-circle arc
    theta1 = 90 * orientation
    theta2 = theta1 + 90
    ax.add_patch(patches.Arc((x + (side if orientation==0 else 0),
                              y + (0 if orientation==0 else side)),
                             2*side, 2*side,
                             angle=0, theta1=theta1, theta2=theta2,
                             color='royalblue'))
    # update for next square
    if orientation == 0:          # right → up
        x += side
    elif orientation == 1:        # up → left
        y += side
        x -= side
    elif orientation == 2:        # left → down
        x -= side
        y -= side
    else:                         # down → right
        y -= side
    orientation = (orientation + 1) % 4

ax.set_aspect('equal')
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
plt.title("Ever-smaller Fibonacci squares and golden-spiral arc")
plt.axis('off')
plt.show()
