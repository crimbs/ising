import numpy as np

def energy(lattice):
    return -1 * lattice * (np.roll(lattice, -1, 0)
                           + np.roll(lattice, +1, 0)
                           + np.roll(lattice, -1, 1)
                           + np.roll(lattice, +1, 1))

def dE(lattice):
    return -2 * energy(lattice)

def boltzmann(E, T=0.1, k=1):
    return np.exp(-E / (k * T))

def evolve(lattice):

    pos = np.greater(boltzmann(dE(lattice)), np.random.rand(*lattice.shape))

    neg = np.less(dE(lattice), np.zeros_like(lattice))

    return np.where(pos + neg, -lattice, lattice)

def main(steps=10**2, N=8):
    lattice = np.random.choice([1, -1], size=(N, N))
    for i in range(steps):
        lattice = evolve(lattice)
    return lattice

test = main()






'''
energy_lattice = energy(lattice)
delta_energy_lattice = dE(lattice)


# upper
boltz_array = boltzmann(delta_energy_lattice, T=1)

boltz_rand = np.random.rand(N, N)

upper = np.greater(boltz_array, boltz_rand)
upper1 = np.greater(boltzmann(delta_energy_lattice, T=1), np.random.rand(N, N))

# lower
zero_lattice = np.zeros(shape=(N, N))

lower = np.less(delta_energy_lattice, zero_lattice)
lower1 = np.less(delta_energy_lattice, np.zeros(shape=(N, N)))

what = lower + upper
'''
