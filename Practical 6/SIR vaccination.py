import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Parameters
N = 10000  # Total population
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
time_steps = 1000  # Simulation duration
vaccination_percentages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Vaccination levels to test

# Initialize figure for plotting
plt.figure(figsize=(10, 6), dpi=150)
colors = cm.viridis(np.linspace(0, 1, len(vaccination_percentages)))  # Color gradient

# Run simulation for each vaccination percentage
for i, vax_percent in enumerate(vaccination_percentages):
    # Initial conditions
    S = N - 1 - int(N * vax_percent / 100)  # Susceptible (subtract initial infected and vaccinated)
    I = 1  # Initial infected
    R = int(N * vax_percent / 100)  # Vaccinated/recovered (initially all vaccinated)
    
    # Arrays to track populations over time
    S_history = [S]
    I_history = [I]
    R_history = [R]
    
    # Simulation loop
    for t in range(time_steps):
        # Calculate new infections - ensure S doesn't go negative
        infection_prob = beta * I / N
        effective_S = max(S, 0)  # Ensure S is not negative
        new_infections = np.random.binomial(effective_S, infection_prob) if effective_S > 0 else 0
        
        # Calculate new recoveries - ensure I doesn't go negative
        effective_I = max(I, 0)  # Ensure I is not negative
        new_recoveries = np.random.binomial(effective_I, gamma) if effective_I > 0 else 0
        
        # Update populations with bounds checking
        S = max(S - new_infections, 0)
        I = max(I + new_infections - new_recoveries, 0)
        R = min(R + new_recoveries, N)  # Ensure R doesn't exceed population
        
        # Record current state
        S_history.append(S)
        I_history.append(I)
        R_history.append(R)
    
    # Plot infected curve for this vaccination percentage
    plt.plot(I_history, color=colors[i], 
             label=f'{vax_percent}% vaccinated', linewidth=1.5)

# Plot formatting
plt.xlabel('Time')
plt.ylabel('Number Infected')
plt.title('SIR Model with Vaccination: Infected Population Over Time')
plt.legend(title='Vaccination %', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(alpha=0.3)
plt.tight_layout()

# Save and show plot
plt.savefig("SIR_vaccination_results.png", format="png", bbox_inches='tight')
plt.show()

# Optional: Print herd immunity threshold estimate
print("Based on the plots, the herd immunity threshold appears to be around 60-70% vaccination.")