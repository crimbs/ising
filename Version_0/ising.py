import numpy as np
import time
#import matplotlib.pyplot as plt
start = time.time()

# Define global variables
N = 4                           # N x N lattice sites
T = 1                           # Temperature [J/k_B]
num_steps = 10**1               # Number of time steps
time_step = N**2
total_steps = num_steps * time_step

# Initialisation of lattice
lattice = np.random.choice([1, -1], size=(N, N))

# Initialisation of random variables outside of loops
lattice_picker = np.random.randint(N, size=(total_steps, 2))
boltzmann_picker = np.random.rand(total_steps)

# Energy of individual spin site (i, j) using 2d Ising Model with J=1
def energy_of_site(i, j):
    return -1 * lattice[i, j] * (lattice[((i - 1) % N), j]
                                 + lattice[((i + 1) % N), j]
                                 + lattice[i, ((j - 1) % N)]
                                 + lattice[i, ((j + 1) % N)])

# Energy required to flip the spin of an individual spin site (i, j)
def energy_required_to_flip(i, j):
    return -2 * energy_of_site(i, j)

# Flips the direction of the spin of an individual spin site (i, j)
def flip_spin(i, j):
    lattice[i, j] = -lattice[i, j]
    return lattice[i, j]

def energy():
    return -1 * lattice * (np.roll(lattice, -1, 0)
                           + np.roll(lattice, +1, 0)
                           + np.roll(lattice, -1, 1)
                           + np.roll(lattice, +1, 1))
    
#--------Thermodynamic quantities----------#
    
def M():
    return np.sum(lattice)

def M_av():
    return np.mean(lattice)

def E():
    return np.sum(energy())

def E_av():
    return np.mean(energy())

#----------MAIN---------------#

def main():
    for step in range(total_steps):
        i = tuple(lattice_picker[step])
        dE = energy_required_to_flip(*i)
        if dE < 0 or np.exp(-dE / T) > boltzmann_picker[step]:
            flip_spin(*i)
    return M(), M_av(), E(), E_av()
    
wuel = main()

end = time.time()
print(end - start)
