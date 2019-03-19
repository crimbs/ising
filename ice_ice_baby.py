# author: Christian Hines
# date: March 2019
# ising.py
import numpy as np

#np.random.seed(seed=1234)
#alternative_random_gen = [-1,1][np.random.randint(2)]

# Define global variables
N = 16                          # N x N lattice sites
T = 0.1                           # Temperature [K]
#k = 1.38064852e-23              # Boltzmann's Constant [m^2 kg s^-2 K^-1]
num_steps = 10**3               # Number of time steps

# Initialisation
lattice = np.random.choice([1, -1], size=(N, N))

for step in range(num_steps):
    
    i = np.random.randint(N)
    j = np.random.randint(N)

    dE = lattice[i,j]*lattice[((i - 1) % N), j] + \
        lattice[((i + 1) % N), j] + \
        lattice[i, ((j - 1) % N)] + \
        lattice[i, ((j + 1) % N)]
        
    if dE < 0 or np.exp(-dE/T) > np.random.rand():
        lattice[i, j] = -lattice[i, j]