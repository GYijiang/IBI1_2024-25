import numpy as np
import matplotlib.pyplot as plt

# Make a 100x100 array of all susceptible population
population = np.zeros((100, 100))

# Randomly select the initial outbreak location
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1  # Set the initial infected person

# Define model parameters
beta = 0.3  # Infection probability
gamma = 0.05  # Recovery probability
time_steps = 100  # Number of time points to simulate

# Create a list to store the population states at each time step
population_history = [population.copy()]

for t in range(time_steps):
    # Create a new array to store the updated population state
    new_population = population.copy()
    
    for i in range(100):
        for j in range(100):
            if population[i, j] == 1:  # If the person is infected
                # Infepct neighbors with probability beta
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue  # Skip the current cell
                        ni, nj = i + di, j + dj
                        if 0 <= ni < 100 and 0 <= nj < 100:
                            if population[ni, nj] == 0:  # Susceptible neighbor
                                if np.random.rand() < beta:
                                    new_population[ni, nj] = 1
                
                # Recover with probability gamma
                if np.random.rand() < gamma:
                    new_population[i, j] = 2
    
    # Update the population for the next time step
    population = new_population
    population_history.append(population.copy())

# Plot the progression of the disease
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
time_points = [0, 10, 50, 99]

for ax, t in zip(axes.flatten(), time_points):
    ax.imshow(population_history[t], cmap='viridis', interpolation='nearest')
    ax.set_title(f'Time Step {t}')
    ax.axis('off')

plt.tight_layout()
plt.show()