import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def initialize_population(size=100):
    population = np.zeros((size, size), dtype=int)
    outbreak = np.random.choice(range(size), 2)
    population[outbreak[0], outbreak[1]] = 1
    return population, outbreak
# Initialize the population with one infected cell
def infect_neighbors(population, i, j, beta):
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:  # Skip self
                continue
            ni, nj = i + di, j + dj
            # Check boundaries and susceptibility
            if 0 <= ni < 100 and 0 <= nj < 100 and population[ni, nj] == 0:
                if np.random.rand() < beta:
                    population[ni, nj] = 1
# Infect the neighbors of an infected cell with probability beta
# This function infects the neighboring cells of an infected cell with a certain probability (beta).
def simulate_spread(population, beta=0.3, gamma=0.05, time_steps=100):
    history = []
    for _ in range(time_steps):
        new_population = population.copy()
        # Find all infected cells
        infected = np.argwhere(population == 1)
        
        for i, j in infected:
            # Infect neighbors
            infect_neighbors(new_population, i, j, beta)
            # Recover with probability gamma
            if np.random.rand() < gamma:
                new_population[i, j] = 2
        
        population = new_population
        history.append(population.copy())
    return history
# Simulate the spread of infection over time
# This function simulates the spread of infection over a specified number of time steps.
def plot_results(history, time_points=[0, 10, 50, 99]):
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    cmap = plt.get_cmap('viridis', 3)  # 3 discrete colors
    
    for ax, t in zip(axes.flatten(), time_points):
        img = ax.imshow(history[t], cmap=cmap, interpolation='nearest', vmin=0, vmax=2)
        ax.set_title(f'Time Step {t}')
        ax.axis('off')
    
    # Add colorbar legend
    cbar = fig.colorbar(img, ax=axes, ticks=[0, 1, 2], shrink=0.6)
    cbar.ax.set_yticklabels(['Susceptible', 'Infected', 'Recovered'])
    plt.tight_layout()
    plt.show()

def main():
    # Initialize parameters
    beta = 0.3
    gamma = 0.05
    time_steps = 100
    
    # Run simulation
    population, outbreak = initialize_population()
    history = simulate_spread(population, beta, gamma, time_steps)
    
    # Visualize results
    plot_results(history)

if __name__ == "__main__":
    main()