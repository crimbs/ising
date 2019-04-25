import numpy as np
import matplotlib.pyplot as plt
import time
import math
from scipy import ndimage


__all__ = ['energy_required_to_flip', 
           'total_magnetisation', 
           'total_energy',
           'getNeighbours',
           'CClabel',
           'domain_size',
           'burn',
           'main']


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


def getNeighbours(N, i, j):
    """
    Returns a list of neighbour coordinates for the site (i, j)
    """
    neighbours = []
    neighbours.append(tuple([(i + 1) % N, j]))
    neighbours.append(tuple([(i - 1) % N, j]))
    neighbours.append(tuple([i, (j - 1) % N]))
    neighbours.append(tuple([i, (j + 1) % N]))
    return neighbours


def CClabel(lattice):
    """
    Connected-component labeling function with periodic boundary conditions
    """
    N = len(lattice)
    labelled = np.zeros_like(lattice)
    todolist = []
    label = 1
    for i in range(N):
        for j in range(N):
            
            if labelled[i][j] == 0:
                labelled[i][j] = label
                todolist.append((i, j))
                
                while todolist:
                    site = todolist.pop(0)
                    neighbours = getNeighbours(N, *site)
                    
                    for k in [0, 1, 2, 3]:
                        if  lattice[neighbours[k]] == lattice[i][j] and \
                            labelled[neighbours[k]] == 0:   
                            labelled[neighbours[k]] = label
                            todolist.append(neighbours[k])
                label += 1
                
    return labelled


def domain_size(lattice, plot=False):
    """
    Returns the Largest Cluster Size
    """
    N = len(lattice)
    labels = CClabel(lattice)
    area = ndimage.measurements.sum(lattice, labels,
                                    index=np.arange(labels.max() + 1))
    out = np.abs(area[labels])

    if plot:
        plt.figure()
        plt.imshow(out, cmap='gray')
        plt.colorbar()
        plt.axis('off')
        plt.title('Lattice Grouped By Domain Size (N=%i)' % N)

    largest_cluster = out.max()

    return largest_cluster


def burn(N, nsites, lattice, T, nburn):
    """
    """
    # Generate random coordinates/test values
    random_site = np.random.randint(N, size=(nburn*nsites, 2))
    boltzmann_picker = np.random.rand(nburn*nsites)
    
    for step in range(nburn*nsites):
        i, j = random_site[step][0], random_site[step][1]
        dE = energy_required_to_flip(lattice, N, i, j)
        if dE < 0 or math.exp(-dE / T) >= boltzmann_picker[step]:
            lattice[i][j] = -lattice[i][j]


def main(N=64, ntimesteps=10**4, Tmin=1, Tmax=5, ntemp=50):
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
    D_arr = np.empty(ntemp)    # Largest domain size per spin

    # Initialisation of lattice
    lattice = np.random.choice([+1, -1], size=(N, N))
    
    burn(N, nsites, lattice, T=Tmin, nburn=1000)
    
    temp_ind = 0        # temperature loop array indexing integer
    
    # Temperature loop
    for T in T_arr:
        
        # Burn in to reach equilibrium
        burn(N, nsites, lattice, T, nburn=1000)

        # Define observables
        Mabs = 0
        Msq = 0
        E = 0
        Esq = 0
        D = 0
        
        # Update random coordinates/test values for main loop
        random_site = np.random.randint(N, size=(total_steps, 2))
        boltzmann_picker = np.random.rand(total_steps)
        
        # Initialise counters
        m = total_magnetisation(lattice)
        e = total_energy(lattice)

        tstep_ind = 0  # timestep loop array indexing integer
        
        # Main timestep loop
        for timestep in range(ntimesteps):
            
            # Do a lattice sweep
            for site in range(nsites):
                i, j = random_site[tstep_ind][0], random_site[tstep_ind][1]
                dE = energy_required_to_flip(lattice, N, i, j)
                if dE < 0 or math.exp(-dE / T) >= boltzmann_picker[tstep_ind]:
                    lattice[i][j] = -lattice[i][j]
                    m += 2 * lattice[i][j]
                    e += 2 * dE
                tstep_ind += 1

            # Update thermodynamic observables
            Mabs += abs(m)
            Msq += m * m
            E += e / 2
            Esq += (e / 2) * (e / 2)
            D += domain_size(lattice)
            
        # Update averages
        Mabs_av = Mabs / total_steps
        Msq_av = Msq / total_steps
        E_av = E / total_steps
        Esq_av = Esq / total_steps
        D_av = D / total_steps
    
        # Place averages into arrays
        Mabs_arr[temp_ind] = Mabs_av
        E_arr[temp_ind] = E_av
        X_arr[temp_ind] = (Msq_av - ((Mabs_av**2) * nsites)) / (T)
        C_arr[temp_ind] = (Esq_av - ((E_av**2) * nsites)) / (T**2)
        D_arr[temp_ind] = D_av
    
        temp_ind += 1
        # end of temperature loop

    # Create master array and save to file
    out = np.vstack((T_arr, Mabs_arr, E_arr, X_arr, C_arr, D_arr)).T
    np.savetxt("N%i" % N, out, header="T, |M|, E, X, C, D")


start = time.time()

if __name__ == "__main__":
    main()
    
print(time.time() - start)
