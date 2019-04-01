# author: Christian Hines
# date: March 2019
# scrapyard.py
import numpy as np
import time
start = time. time()

# Define global variables
N = 8                           # N x N lattice sites
T = 1                           # Temperature [J/k_B]
num_steps = 10**3               # Number of time steps
time_step = N**2
total_steps = num_steps*time_step

# Initialisation
lattice = np.random.choice([1, -1], size=(N, N))

lattice_picker = np.random.randint(N, size=(total_steps, 2))

boltzmann_picker = np.random.rand(total_steps)

# Energy function
def dE(i, j):
    return lattice[i, j] * lattice[((i - 1) % N), j] + \
        lattice[((i + 1) % N), j] + \
        lattice[i, ((j - 1) % N)] + \
        lattice[i, ((j + 1) % N)]

# Metropolis-Hastings Algorithm (very slightly slower)
for step in range(num_steps*(N**2)):
    
    i = tuple(lattice_picker[step])
    
    dE = lattice[i] * lattice[((i[0] - 1) % N), i[1]] + \
        lattice[((i[0] + 1) % N), i[1]] + \
        lattice[i[0], ((i[1] - 1) % N)] + \
        lattice[i[0], ((i[1] + 1) % N)]
     
    if dE < 0 or np.exp(-dE/T) > boltzmann_picker[step]:
        lattice[i] = -lattice[i]

what= np.sum(lattice)
            
end = time.time()
print(end - start)