import numpy as np


def energy_required_to_flip(lattice, N, i, j):
    '''
    Energy required to flip the spin of an individual spin site (i, j)
    '''
    lat = np.array(lattice)
    energy_of_site = -1 * lat[i][j] * (lat[((i - 1) % N)][j]
                                       + lat[((i + 1) % N)][j]
                                       + lat[i][((j - 1) % N)]
                                       + lat[i][((j + 1) % N)])
    dE = -2 * energy_of_site
    return dE


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


def evolve(lat, T=1, n=1, everystep=False):
    """
    Evolve the lattice using metropolis algorithm
    """
    lattice = lat
    N = len(lattice)

    if everystep:
        for step in range(n):
            i = np.random.randint(N, size=(2))
            dE = energy_required_to_flip(lattice, N, *i)
            if dE < 0 or np.exp(-dE / T) > np.random.rand():
                flip_spin(lattice, *i)
            return lattice

    else:
        for step in range(n):
            i = np.random.randint(N, size=(2))
            dE = energy_required_to_flip(lattice, N, *i)
            if dE < 0 or np.exp(-dE / T) > np.random.rand():
                flip_spin(lattice, *i)
        return lattice


def main(
        N=4,
        T=1,
        nsteps=10**2,
        mag=True,
        energy=False,
        burn=True,
        nburn=10**4,
        everystep=False):
    """
    Returns the two-dimensional array [Magnetisation,Energy]
    """
    temp = T

    # Initialisation of lattice
    lattice = np.random.choice([1, -1], size=(N, N))

    # Burn-in to reach equilibrium
    if burn:
        lattice = evolve(lat=lattice, T=temp, n=nburn, everystep=False)

    # Return various thermodynaimc quantities every step or every sweep
    def metropolis():
        if everystep:
            evolved_lattice = evolve(lat=lattice, T=temp, n=1, everystep=True)
            return M(evolved_lattice)
        else:
            evolved_lattice = evolve(
                lat=lattice, T=temp, n=N**2, everystep=False)

        if mag and energy:
            return M(evolved_lattice), E(evolved_lattice)
        elif energy:
            return E(evolved_lattice)
        elif mag:
            return M(evolved_lattice)

    out = np.array([metropolis() for step in range(nsteps)]).T

    return out
