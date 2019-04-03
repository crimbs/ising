import numpy as np


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
    lattice[i][j] = -lattice[i][j]
    return lattice[i][j]


def M(lattice):
    '''
    Returns total magnetisation of the system
    '''
    return np.sum(lattice)


def E(lattice):
    '''
    Returns total energy of the system
    '''
    energy_array = -1 * lattice * (np.roll(lattice, -1, 0)
                                   + np.roll(lattice, +1, 0)
                                   + np.roll(lattice, -1, 1)
                                   + np.roll(lattice, +1, 1))
    return np.sum(energy_array)


def main(N=4, T=1, nsteps=10**2):
    '''
    Returns the two-dimensional array [Magnetisation,Energy]
    '''
    # Initialisation of lattice
    lattice = np.random.choice([1, -1], size=(N, N))

    def metropolis():
        for step in range(N**2):
            i = np.random.randint(N, size=(2))
            dE = energy_required_to_flip(lattice, N, *i)
            if dE < 0 or np.exp(-dE / T) > np.random.rand():
                flip_spin(lattice, *i)

        return M(lattice), E(lattice)
    return np.array([metropolis() for step in range(nsteps)]).T
