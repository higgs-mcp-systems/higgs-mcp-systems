import numpy as np

import time



# Set the seed for reproducibility

np.random.seed(0)



# Define the Higgs field parameters

higgs_field_strength = 1.0

higgs_field_frequency = 1.0



# Define the particle properties

num_particles = 10**7

particle_mass = 1.0

particle_charge = 1.0



# Initialize the particle positions and velocities

positions = np.random.uniform(-10, 10, size=(num_particles, 3))

velocities = np.random.uniform(-1, 1, size=(num_particles, 3))



# Define the time step and total simulation time

dt = 0.01

total_time = 10.0



# Initialize the simulation time array

time_array = np.arange(0, total_time, dt)



# Simulate the particle trajectory

start_time = time.time()

for t in time_array:

    # Calculate the Higgs field at each particle position

    higgs_field = higgs_field_strength * np.sin(higgs_field_frequency * t) * np.ones((num_particles, 3))



    # Update the particle velocities using the Higgs field

    velocities += higgs_field * dt



    # Update the particle positions using the updated velocities

    positions += velocities * dt



# Print the simulation time

print(f"Simulation time: {time.time() - start_time} seconds")



# Save the final particle positions and velocities to a file

np.save("final_positions.npy", positions)

np.save("final_velocities.npy", velocities)
