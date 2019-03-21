# author: Christian Hines
# date: March 2019
# ising.py
import numpy as np
import time
start = time. time()

# Define global variables
N = 8                           # N x N lattice sites
T = 1                           # Temperature [K]
num_steps = 10**3               # Number of time steps

# Initialisation
lattice = np.int8(np.random.choice([1, -1], size=(N, N)))

# Metropolis-Hastings Algorithm
for step in range(num_steps):
    
    for k in range(N**2):
        
        i, j = np.random.randint(N), np.random.randint(N)
    
        dE = lattice[i,j] * lattice[((i - 1) % N), j] + \
            lattice[((i + 1) % N), j] + \
            lattice[i, ((j - 1) % N)] + \
            lattice[i, ((j + 1) % N)]
            
        if dE < 0 or np.exp(-dE/T) > np.random.rand():
            lattice[i, j] = -lattice[i, j]
   
         
end = time. time()
print(end - start)