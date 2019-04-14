import numpy as np
import time
import math
import domainsize

__all__ = ['energy_required_to_flip', 
           'total_magnetisation', 
           'burn',
           'main']

def energy_required_to_flip(lattice, N, i, j):
    """
    Energy required to flip the spin of an individual spin site (i, j)
    """
    dE = 2 * lattice[i][j] * (lattice[((i - 1) % N)][j]
                              + lattice[((i + 1) % N)][j]
                              + lattice[i][((j - 1) % N)]
                              + lattice[i][((j + 1) % N)])
    return dE


def total_magnetisation(lattice):
    """
    Returns total magnetisation of the system
    """
    return np.sum(lattice)



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


def main(N=8, ntimesteps=10**1, T=2.5, metropolis=True, wolff=False):
    """
    Implements the metropolis algorithm and saves data to file
    """
    nsites = N**2
    total_steps = ntimesteps * nsites

    # steps array to be used in loop
    nsteps = np.arange(total_steps, dtype=float)
    
    # Initialise arrays
    Mabs_arr = np.empty(total_steps)  # Absolute magnetisation per spin

    # Initialisation of lattice
    lattice = np.random.choice([+1, -1], size=(N, N))
        
    # Burn in to reach equilibrium
    burn(N, nsites, lattice, T, nburn=1000)
    
    # Update random coordinates/test values for main loop
    random_site = np.random.randint(N, size=(total_steps, 2))
    boltzmann_picker = np.random.rand(total_steps)
    
    m = total_magnetisation(lattice)

    tstep_ind = 0  # timestep loop array indexing integer
    
    if metropolis:
        # Main timestep loop
        for timestep in nsteps:
            
            i, j = random_site[tstep_ind][0], random_site[tstep_ind][1]
            dE = energy_required_to_flip(lattice, N, i, j)
            if dE < 0 or math.exp(-dE / T) >= boltzmann_picker[tstep_ind]:
                lattice[i][j] = -lattice[i][j]
                m += 2 * lattice[i][j]
        
            # Place obseravables into arrays
            Mabs_arr[tstep_ind] = abs(m) / nsites
            
            tstep_ind += 1
    
    elif wolff:
        # Wolff Algorithm variables
        cluster_size = 0
        p = 1 - math.exp(-2/T)
        todolist = []
        label = 1
        ind = 0
        for timestep in nsteps:
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
            
            cluster_size += np.sum(labelled)
            
            # Place obseravables into arrays
            Mabs_arr[ind] = np.abs(total_magnetisation(lattice)) / nsites
            ind += 1
        
        timestep_sf = (total_steps * nsites) / cluster_size
        
        nsteps *= timestep_sf
        
    # Create master array and save to file
    out = np.vstack((nsteps, Mabs_arr)).T
    np.savetxt("acf_N%0.0f" % N, out, header="Steps, |M|")
    
    return out

start = time.time()

if __name__ == "__main__":
    main(N=16, ntimesteps=10**1, T=2.5, metropolis=False, wolff=True)
    
print(time.time() - start)