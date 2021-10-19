import numpy as np
import time
import math
import ising


def main(N=4, ntimesteps=500, T=2.5):
    """
    Function which implements the Wolff Algorithm and saves the 
    Absolute Magnetisation per spin into a .txt file under the 
    name 'mag_N<lattice size>.txt' (e.g. mag_N8.txt for an 
    8 x 8 lattice). This can then be loaded using numpy.loadtxt 
    into other scripts as a numpy array (and subsequently indexed 
    for the relevant observables).
    -----------------------------
    Parameters
    -----------------------------
    N :             Lattice size (i.e. N x N lattice)
    ntimesteps :    Number of time steps (i.e. sweeps of the lattice)
    T :             Temperature
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
    ising.burn(N, nsites, lattice, T, nburn=1000)

    tstep_ind = 0  # timestep loop array indexing integer
    
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
                neighbours = ising.getNeighbours(N, *site)
                
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
        Mabs_arr[ind] = np.abs(ising.total_magnetisation(lattice)) / nsites
        ind += 1
    
    timestep_sf = (total_steps * nsites) / cluster_size
    
    nsteps *= timestep_sf
        
    # Create master array and save to file
    out = np.vstack((nsteps, Mabs_arr)).T
    np.savetxt("mag_N%i" %N, out, header="Steps, |M|")


start = time.time()

if __name__ == "__main__":
    main()
    
print(time.time() - start)