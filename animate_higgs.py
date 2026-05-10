import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Setup 50,000 particles for smooth animation
num_particles = 50000
positions = np.random.uniform(-10, 10, size=(num_particles, 3))
velocities = np.random.uniform(-0.1, 0.1, size=(num_particles, 3))

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
scat = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], c='blue', s=0.5, alpha=0.6)

ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_zlim(-15, 15)

def update(frame):
    global positions, velocities
    # Simulate the Higgs Field "Pulse"
    field_effect = 0.05 * np.sin(frame * 0.1)
    velocities += field_effect * 0.1
    positions += velocities

    # Update the visual dots
    scat._offsets3d = (positions[:, 0], positions[:, 1], positions[:, 2])
    return scat,

# 100 frames of motion
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=False)
print("Saving animation... this may take a minute.")
ani.save('higgs_field_simulation.mp4', writer='ffmpeg', fps=30)
print("Done! Check your folder for higgs_field_simulation.mp4")
