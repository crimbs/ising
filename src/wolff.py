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
    Returns energy required to flip the spin of an 
    individual spin site (i, j). Toroidal periodic
    boundary conditions are imposed.
    """
    dE = 2. * lattice[i][j] * (lattice[((i - 1) % N)][j]
                              + lattice[((i + 1) % N)][j]
                              + lattice[i][((j - 1) % N)]
                              + lattice[i][((j + 1) % N)])
    return dE


def total_magnetisation(lattice):
    """
    Returns total magnetisation of a given lattice
    """
    return np.sum(lattice)



def burn(N, nsites, lattice, T, nburn):
    """
    Function which iterates the Metropolis algorithm
    to `burn-in' the lattice to reach equilibrium.
    -----------------------------
    Parameters
    -----------------------------
    N :         Lattice size (i.e. N x N lattice)
    nsites :    Number of sites on the lattice (i.e. N^2)
    lattice :   N x N numpy array of +1 or -1 values
    T :         Temperature
    nburn :     Number of iterations to reach equilibrium
    """
    # Generate random coordinates/test values
    random_site = np.random.randint(N, size=(nburn*nsites, 2))
    boltzmann_picker = np.random.rand(nburn*nsites)
    
    for step in range(nburn*nsites):
        i, j = random_site[step][0], random_site[step][1]
        dE = energy_required_to_flip(lattice, N, i, j)
        if dE < 0 or math.exp(-dE / T) >= boltzmann_picker[step]:
            lattice[i][j] = -lattice[i][j]


def main(N=4, ntimesteps=500, T=2.5, metropolis=False, wolff=True):
    """
    Function which implements either the Metropolis algorithm or 
    the Wolff Algorithm and saves the Absolute Magnetisation per spin
    into a .txt file under the name 'mag_N<lattice size>.txt' 
    (e.g. mag_N8.txt for an 8 x 8 lattice). This can then be
    loaded using numpy.loadtxt into other scripts as a numpy array 
    (and subsequently indexed for the relevant observables).
    -----------------------------
    Parameters
    -----------------------------
    N :             Lattice size (i.e. N x N lattice)
    ntimesteps :    Number of time steps (i.e. sweeps of the lattice)
    T :             Temperature
    metropolis :    Boolean (default False) Use Metropolis algorithm
    wolff :         Boolean (default True) Use Wolff algorithm
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
    np.savetxt("mag_N%i" % N, out, header="Steps, |M|")
    
    return out

start = time.time()

if __name__ == "__main__":
    main()
    
print(time.time() - start)