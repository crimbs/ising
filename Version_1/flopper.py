import numpy as np
import time
import ising

def M(lattice): 
    return np.sum(lattice) / (len(lattice)**2)

def E(lattice):
    '''
    Returns total energy of the system
    '''
    energy_array = -1 * lattice * (np.roll(lattice, -1, 0)
                                   + np.roll(lattice, +1, 0)
                                   + np.roll(lattice, -1, 1)
                                   + np.roll(lattice, +1, 1))
    return np.sum(energy_array)

def metropolis_using_roll(N=4, T=1, nsteps=10**1):

    N=N
    T=T
    tsteps=nsteps
    
    # initialize
    lattice = np.random.choice([1, -1], size=(N, N))
    newlattice = np.empty_like(lattice)
    M_arr = np.empty(shape=tsteps)
#    E_arr = np.empty(shape=tsteps)
    
    for i in range(tsteps):
        
        for j in range(N**2):
            # lattice energy
            lattice_energy = E(lattice)
            
            # make a copy of lattice called 'newlattice'
            np.copyto(newlattice, lattice)
            
            # pick a random spin on 'lattice copy' and flip it
            x, y = np.random.randint(N), np.random.randint(N)
            newlattice[x][y] = - newlattice[x][y]
            
            # proposed lattice energy
            new_lattice_energy = E(newlattice)
            
            # change in energy
            dE = new_lattice_energy - lattice_energy
            
            # whether to accept proposed lattice 
            if dE < 0 or np.exp(-dE / T) > np.random.rand():
                lattice, newlattice = newlattice, lattice
                
        M_arr[i] = M(lattice)
#        E_arr[i] = E(lattice)
        
    return M_arr
