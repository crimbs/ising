
import numpy as np
import matplotlib.pyplot as plt


# Define global variables
N = 100                           # N x N lattice sites

# Initialisation of lattice
lattice = np.random.choice([1, -1], size=(N, N))

plt.plot(lattice)
plt.savefig('randomness.pdf')
