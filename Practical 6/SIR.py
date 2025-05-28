import numpy as np
import matplotlib.pyplot as plt

def sir_euler(S0, I0, R0, beta, gamma, days):
    N = S0 + I0 + R0
    S = S0
    I = I0
    R = R0
    S_list = [S0]
    I_list = [I0]
    R_list = [R0]
    # Simulate the SIR model using Euler's method
    for i in range(days):
 # Simulate the SIR model using Euler's method      
        infected_prob = beta * I / N
        inf_list = np.random.choice(range(2), S, p=[1-infected_prob, infected_prob])
        S -= np.sum(inf_list)
        reco_list = np.random.choice(range(2), I, p=[1-gamma, gamma])
        R += np.sum(reco_list)  
        I += np.sum(inf_list) - np.sum(reco_list)
# Ensure populations do not go negative
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
    return S_list, I_list, R_list
# SIR Model using Euler's method for simulation of disease spread
beta = 0.3 
gamma = 0.05 
# Initial conditions
N = 10000
I0 = 1
R0 = 0
S0 = N - I0 - R0
days = 1000
# Simulate the SIR model
S,I,R = sir_euler(S0, I0, R0, beta, gamma, days)
plt.figure(figsize=(10,6))
plt.plot(S, 'b', label='Susceptible')
plt.plot(I, 'r', label='Infected')
plt.plot(R, 'g', label='Recovered')
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.title('SIR Model (Euler Method)')
plt.legend()
plt.grid()
plt.show()
# This code simulates the SIR model using Euler's method and plots the results.