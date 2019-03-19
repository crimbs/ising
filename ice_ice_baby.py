# author: Christian Hines
# date: March 2019
# ising.py
import numpy as np

np.random.seed(seed=1234)
#alternative_random_gen = [-1,1][np.random.randint(2)]

# Define global variables
N = 16                  # N x N lattice sites
T = 1                   # Temperature [K]
k = 1.38064852e-23      # Boltzmann's Constant [m^2 kg s^-2 K^-1]
n = 10**2               # Number of time steps

# Initialisation
def lattice(N):
    a = np.random.randint(2, size=(N,N))
    return np.where(a==0, -1, a)

lattice = lattice(N)

for j in range(n):
    for i in range(N):
        for j in range(N):
            E = lattice[((i - 1) % N), j] + \
                lattice[((i + 1) % N), j] + \
                lattice[i, ((j - 1) % N)] + \
                lattice[i, ((j + 1) % N)]
            if E < 0:
                lattice[i, j] = -lattice[i, j]
            else:
                if np.exp(-E/(k*T)) > np.random.rand():
                    lattice[i, j] = -lattice[i, j]
