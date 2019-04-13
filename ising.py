import numpy as np
import time

__all__ = ['energy_required_to_flip', 
           'total_magnetisation', 
           'total_energy', 
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


def total_energy(lattice):
    """
    Returns total energy of the system
    """
    energy_array = -1 * lattice * (np.roll(lattice, -1, 0)
                                   + np.roll(lattice, +1, 0)
                                   + np.roll(lattice, -1, 1)
                                   + np.roll(lattice, +1, 1))
    return np.sum(energy_array)


def main(N=4, ntimesteps=10**3, Tmin=1, Tmax=5, ntemp=1):
    """
    Implements the metropolis algorithm and saves data to file
    """
    nsites = N**2
    total_steps = ntimesteps * nsites
    nburn = 1000

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

        # Generate random coordinates/test values
        random_site = np.random.randint(N, size=(nburn*nsites, 2))
        boltzmann_picker = np.random.rand(nburn*nsites)
        
        # Burn-in to reach equilibrium
        for step in range(nburn*nsites):
            i, j = random_site[step][0], random_site[step][1]
            dE = energy_required_to_flip(lattice, N, i, j)
            if dE < 0 or np.exp(-dE / T) >= boltzmann_picker[step]:
                lattice[i][j] = -lattice[i][j]

        # Define thermodynamic observables
        m = total_magnetisation(lattice)
        e = total_energy(lattice)
        Mabs = 0
        Msq = 0
        E = 0
        Esq = 0
        
        # Update random coordinates/test values for main loop
        random_site = np.random.randint(N, size=(total_steps, 2))
        boltzmann_picker = np.random.rand(total_steps)
        
        tstep_ind = 0  # timestep loop array indexing integer

        # Main timestep loop
        for timestep in range(ntimesteps):

            # Do a lattice sweep
            for site in range(nsites):
                i, j = random_site[tstep_ind][0], random_site[tstep_ind][1]
                dE = energy_required_to_flip(lattice, N, i, j)
                if dE < 0 or np.exp(-dE / T) >= boltzmann_picker[tstep_ind]:
                    lattice[i][j] = -lattice[i][j]
                    m += 2 * lattice[i][j]
                    e += 2 * dE
                # End of lattice sweep loop

            # Update thermodynamic observables
            Mabs += abs(m)
            Msq += m**2
            E += e / 2
            Esq += (e / 2)**2

            tstep_ind += 1
            # End of time step loop

        # Update averages
        Mabs_av = Mabs / total_steps
        Msq_av = Msq / total_steps
        E_av = E / total_steps
        Esq_av = Esq / total_steps

        # Place obseravables into arrays
        Mabs_arr[temp_ind] = Mabs_av
        E_arr[temp_ind] = E_av
        X_arr[temp_ind] = (Msq_av - ((Mabs_av**2) * nsites)) / (T)
        C_arr[temp_ind] = (Esq_av - ((E_av**2) * nsites)) / (T**2)

        temp_ind += 1
        # end of temperature loop

    # Create master array and save to file
    out = np.vstack((T_arr, Mabs_arr, E_arr, X_arr, C_arr)).T
    np.savetxt("N%0.0f" % N, out, header="T, |M|, E, X, C")


start = time.time()

if __name__ == "__main__":
    main()
    
print(time.time() - start)
