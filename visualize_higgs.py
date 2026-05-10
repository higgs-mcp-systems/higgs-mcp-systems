import numpy as np
import matplotlib.pyplot as plt

# Load your 229MB data
data = np.load("final_positions.npy")

# Subsample 10,000 points to keep things fast
subsample = data[np.random.choice(data.shape[0], 10000, replace=False)]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plotting the points
ax.scatter(subsample[:, 0], subsample[:, 1], subsample[:, 2], c='blue', s=1, alpha=0.5)

ax.set_title("Higgs Field Particle Distribution (Subsampled 10k)")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
