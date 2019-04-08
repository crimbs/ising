import numpy as np
import time


def energy_required_to_flip(lattice, N, i, j):
    '''
    Energy required to flip the spin of an individual spin site (i, j)
    '''
    dE = 2 * lattice[i][j] * (lattice[((i - 1) % N)][j]
                              + lattice[((i + 1) % N)][j]
                              + lattice[i][((j - 1) % N)]
                              + lattice[i][((j + 1) % N)])
    return dE


def total_magnetisation(lattice):
    '''
    Returns total magnetisation of the system
    '''
    return np.sum(lattice)


def total_energy(lattice):
    '''
    Returns total energy of the system
    '''
    energy_array = -1 * lattice * (np.roll(lattice, -1, 0)
                                   + np.roll(lattice, +1, 0)
                                   + np.roll(lattice, -1, 1)
                                   + np.roll(lattice, +1, 1))
    return np.sum(energy_array)


def main(N=4, nburn=10**3, T=2.5):

    nsites = N**2
    total_steps = nburn * nsites
    
    # Initialise arrays
    Steps_arr = np.arange(total_steps)
    Mabs_arr = np.empty(total_steps)

    # Initialisation of lattice
    lattice = np.random.choice([1, -1], size=(N, N))    
    
    # Burn-in to reach equilibrium
    random_site = np.random.randint(N, size=(nburn*nsites, 2))
    for step in range(total_steps):
        
        i, j = random_site[step][0], random_site[step][1]
        dE = energy_required_to_flip(lattice, N, i, j)
        if dE < 0 or np.exp(-dE / T) >= np.random.rand():
            lattice[i][j] = -lattice[i][j]
            
        # Place obseravables into arrays
        Mabs_arr[step] = np.abs(total_magnetisation(lattice)) / nsites


    # create one master array to be returned
    out = np.vstack((Steps_arr, Mabs_arr)).T

    return out

import matplotlib.pyplot as plt

for n in np.arange(2,16)[0::4]:
    test = main(N=n, nburn=1000, T=2.5).T

    plt.figure()
    plt.plot(test[0], test[1])

