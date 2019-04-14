import numpy as np
import time
import math
import domainsize
import matplotlib.pyplot as plt


def energy_required_to_flip(lattice, N, i, j):
    """
    Energy required to flip the spin of an individual spin site (i, j)
    """
    dE = 2. * lattice[i][j] * (lattice[((i - 1) % N)][j]
                              + lattice[((i + 1) % N)][j]
                              + lattice[i][((j - 1) % N)]
                              + lattice[i][((j + 1) % N)])
    return dE


def total_magnetisation(lattice):
    """
    Returns total magnetisation of the system
    """
    return np.sum(lattice)


def total_energy(lattice):
    """
    Returns total energy of the system
    """
    energy_array = -1. * lattice * (np.roll(lattice, -1, 0)
                                   + np.roll(lattice, +1, 0)
                                   + np.roll(lattice, -1, 1)
                                   + np.roll(lattice, +1, 1))
    return np.sum(energy_array)


def burn(N, nsites, lattice, T, nburn):
    """
    """
    # Generate random coordinates/test values for burn-in
    random_site = np.random.randint(N, size=(nburn*nsites, 2))
    boltzmann_picker = np.random.rand(nburn*nsites)
    
    for step in range(nburn*nsites):
        i, j = random_site[step][0], random_site[step][1]
        dE = energy_required_to_flip(lattice, N, i, j)
        if dE < 0 or math.exp(-dE / T) >= boltzmann_picker[step]:
            lattice[i][j] = -lattice[i][j]



N=4
ntimesteps=10**2
Tmin=1 
Tmax=5 
ntemp=5
"""
Implements the metropolis algorithm and saves data to file
"""
nsites = N * N
total_steps = ntimesteps * nsites

# Temperature array to be used in loop
T_arr = np.linspace(Tmin, Tmax, num=ntemp)

# Initialise arrays
Mabs_arr = np.empty(ntemp)  # Absolute magnetisation per spin
E_arr = np.empty(ntemp)     # Energy per spin
X_arr = np.empty(ntemp)     # Susceptibility per spin
C_arr = np.empty(ntemp)     # Heat capcity per spin

# Initialisation of lattice
lattice = np.random.choice([+1, -1], size=(N, N))

temp_ind = 0        # temperature loop array indexing integer

# Temperature loop
for T in T_arr:
    
    # Burn in to reach equilibrium
    burn(N, nsites, lattice, T, nburn=1000)

    # Define thermodynamic observables
    Mabs = 0
    Msq = 0
    E = 0
    Esq = 0
    
    tstep_ind = 0  # timestep loop array indexing integer

    # Wolff Algorithm variables
    p = 1 - math.exp(-2/T)
    todolist = []
    label = 1
    
    for timestep in range(ntimesteps):
        labelled = np.zeros_like(lattice)
        i, j = np.random.randint(N), np.random.randint(N)
        if labelled[i][j] == 0:
            labelled[i][j] = label
            todolist.append((i, j))
            
            while todolist:
                site = todolist.pop(0)
                neighbours = domainsize.getNeighbours(N, *site)
                
                for k in [0, 1, 2, 3]:
                    if  lattice[neighbours[k]] == lattice[i][j] and \
                        labelled[neighbours[k]] == 0 and \
                        p >= np.random.rand():   
                        labelled[neighbours[k]] = label
                        todolist.append(neighbours[k])
                    tstep_ind += 1
        
        # Flip cluster
        lattice = np.where(labelled, -lattice, lattice)
        
        # Update thermodynamic observables
        Mabs += np.abs(total_magnetisation(lattice))
        Msq += np.abs(total_magnetisation(lattice))**2
        E += total_energy(lattice) / 2
        Esq += (total_energy(lattice) / 2)**2
            
    # Update averages
    Mabs_av = Mabs / total_steps
    Msq_av = Msq / total_steps
    E_av = E / total_steps
    Esq_av = Esq / total_steps
        
    # Place averages into arrays
    Mabs_arr[temp_ind] = Mabs_av
    E_arr[temp_ind] = E_av
    X_arr[temp_ind] = (Msq_av - ((Mabs_av**2) * nsites)) / (T)
    C_arr[temp_ind] = (Esq_av - ((E_av**2) * nsites)) / (T**2)
    
    temp_ind += 1
    # end of temperature loop

# Create master array and save to file
out = np.vstack((T_arr, Mabs_arr, E_arr, X_arr, C_arr)).T
np.savetxt("N%0.0f" % N, out, header="T, |M|, E, X, C")

plt.figure()
plt.plot(out.T[0], out.T[1])
plt.figure()
plt.plot(out.T[0], out.T[2])
plt.figure()
plt.plot(out.T[0], out.T[3])
plt.figure()
plt.plot(out.T[0], out.T[4])