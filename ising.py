# author: Christian Hines
# date: March 2019
# ising.py
import numpy as np

np.random.seed(seed=1234)
#alternative_random_gen = [-1,1][np.random.randint(2)]

# Define global variables
N = 31
T = 300     # Temperature [K]
k = 1       # Boltzmann's Constant

# Initialisation
a = np.random.randint(2, size=(N,N))
lattice = np.where(a==0, -1, a)

def E(i,j):
    '''Returns the energy at the i,jth site'''
    return lattice[((i - 1) % N), j] + lattice[((i + 1) % N), j] + \
                    lattice[i, ((j - 1) % N)] + lattice[i, ((j + 1) % N)]

E_Total = 0
for i in range(N):
    for j in range(N):
        E_Total += E(i,j)

whatis = lattice[1,1]
also = E(1,1)
#lattice[1,1] = -lattice[1,1]

E_new = 0
for i in range(N):
    for j in range(N):
        E_new += E(i,j)
'''
if E_new >= E_Total:
    P = np.exp(-(1/(k*T))*(E_new - E_Total))
    if np.random.rand() >= P:
        lattice[0,1] = -lattice[0,1]
    '''