#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Christian Hines'
__date__ = '1st April 2019'

import numpy as np
import matplotlib.pyplot as plt
import time
start = time.time()

# Define global variables
N = 8                           # N x N lattice sites
T = 5                           # Temperature [J/k_B]
num_steps = 10**3               # Number of time steps
time_step = N**2
total_steps = num_steps * time_step


# Initialisation of lattice
lattice = np.random.choice([1, -1], size=(N, N))

# Initialisation of random variables outside of loops
lattice_picker = np.random.randint(N, size=(total_steps, 2))
boltzmann_picker = np.random.rand(total_steps)


# Energy of individual spin site (i, j) using 2d Ising Model with J=1
def E(i, j):
    return -1 * lattice[i, j] * (lattice[((i - 1) % N), j]
                                 + lattice[((i + 1) % N), j]
                                 + lattice[i, ((j - 1) % N)]
                                 + lattice[i, ((j + 1) % N)])


# Energy required to flip the spin of an individual spin site (i, j)
def energy_required_to_flip(i, j):
    return -2 * E(i, j)


# Flips the direction of the spin of an individual spin site (i, j)
def flip_spin(i, j):
    lattice[i, j] = -lattice[i, j]
    return lattice[i, j]


# Total energy of the lattice
def total_energy():
    e = 0
    for i in range(N):
        for j in range(N):
            e += E(i, j)
    return e

# Total magnetisation of the lattice
def total_magnetisation():
    return np.sum(lattice)

def M(step):
    i = tuple(lattice_picker[step])
    dE = energy_required_to_flip(*i)
    if dE < 0 or np.exp(-dE / T) > boltzmann_picker[step]:
        flip_spin(*i)
    return np.sum(lattice)

magnetisation = np.array([M(step) for step in range(total_steps)])

plt.figure()
plt.plot(magnetisation[0::N**2][0::2])
plt.xlabel('time steps')
plt.ylabel('$M$')
plt.savefig('mag_equilibrium.pdf')

'''
# Monte-Carlo Algorithm
for step in range(total_steps):
    i = tuple(lattice_picker[step])
    dE = energy_required_to_flip(*i)
    if dE < 0 or np.exp(-dE/T) > boltzmann_picker[step]:
        flip_spin(*i)

def M(step):
    i = tuple(lattice_picker[step])
    dE = energy_required_to_flip(*i)
    if dE < 0 or np.exp(-dE / T) > boltzmann_picker[step]:
        flip_spin(*i)
    return np.sum(lattice)

test = np.array([M(step) for step in range(total_steps)])


plt.figure()
plt.plot(test[0::10])
plt.ylim(-time_step - 10, +time_step + 10)
from matplotlib2tikz import save as tikz_save
tikz_save('testpgf.tex', figurewidth='\linewidth')

T_array = np.linspace(0.001,10,num=50)


def temp_dependency(T):
    for step in range(10**3):
        i = tuple(lattice_picker[step])
        dE = energy_required_to_flip(*i)
        if dE < 0 or np.exp(-dE/T) > boltzmann_picker[step]:
            flip_spin(*i)
    return np.sum(lattice)

'''
end = time.time()
print(end - start)
