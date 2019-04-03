import numpy as np
import time

#----------DEFINE FUCNTIONS---------------#

def energy_required_to_flip(lattice, N, i, j):
    '''
    Energy required to flip the spin of an individual spin site (i, j)
    '''
    energy_of_site = -1 * lattice[i][j] * (lattice[((i - 1) % N)][j]
                                           + lattice[((i + 1) % N)][j]
                                           + lattice[i][((j - 1) % N)]
                                           + lattice[i][((j + 1) % N)])
    return -2 * energy_of_site


def flip_spin(lattice, i, j):
    '''
    Flips the direction of the spin of an individual spin site (i, j)
    '''
    lattice[i, j] = -lattice[i, j]
    return lattice[i, j]


def energy(lattice):
    '''
    returns an N x N lattice of energy values
    '''
    return -1 * lattice * (np.roll(lattice, -1, 0)
                           + np.roll(lattice, +1, 0)
                           + np.roll(lattice, -1, 1)
                           + np.roll(lattice, +1, 1))

#--------Thermodynamic quantities----------#

def M(lattice):
    return np.sum(lattice)


def M_av(lattice):
    return np.mean(lattice)


def E(lattice):
    return np.sum(energy(lattice))


def E_av(lattice):
    return np.mean(energy(lattice))



#----------MAIN---------------#

def main(N=4, T=1, num_steps=10**1):
    
    time_step = N**2
    total_steps = num_steps * time_step
    
    # Initialisation of lattice
    lattice = np.random.choice([1, -1], size=(N, N))

    # Initialisation of random variables outside of loops
    lattice_picker = np.random.randint(N, size=(total_steps, 2))
    boltzmann_picker = np.random.rand(total_steps)
    
    def metropolis(step):
        i = tuple(lattice_picker[step])
        dE = energy_required_to_flip(lattice, N, *i)
        if dE < 0 or np.exp(-dE / T) > boltzmann_picker[step]:
            flip_spin(lattice, *i)
            
        return M(lattice), M_av(lattice), E(lattice), E_av(lattice)

    return np.array([metropolis(step) for step in range(total_steps)])

def main_alt(N=4, T=1, num_steps=10**1):
    
    # Initialisation of lattice
    lattice = np.random.choice([1, -1], size=(N, N))

    def metropolis():
        for step in range(N**2):
            i = np.random.randint(N, size=(2))
            dE = energy_required_to_flip(lattice, N, *i)
            if dE < 0 or np.exp(-dE / T) > np.random.rand():
                flip_spin(lattice, *i)
            
        return M(lattice), M_av(lattice), E(lattice), E_av(lattice)

    return np.array([metropolis() for step in range(num_steps)])


