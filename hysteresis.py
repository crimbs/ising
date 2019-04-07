import numpy as np


def energy_required_to_flip(lattice, N, i, j, H):
    '''
    Energy required to flip the spin of an individual spin site (i, j)
    '''
    lat = np.array(lattice)
    energy_of_site = -1 * lat[i][j] * (lat[((i - 1) % N)][j]
                                       + lat[((i + 1) % N)][j]
                                       + lat[i][((j - 1) % N)]
                                       + lat[i][((j + 1) % N)]
                                       + H)
    dE = -2 * energy_of_site
    return dE


def total_magnetisation(lattice):
    '''
    Returns total magnetisation of the system
    '''
    return np.sum(lattice)


def total_energy(lattice, H):
    '''
    Returns total energy of the system
    '''
    energy_array = -1 * lattice * (np.roll(lattice, -1, 0)
                                   + np.roll(lattice, +1, 0)
                                   + np.roll(lattice, -1, 1)
                                   + np.roll(lattice, +1, 1)
                                   + H)
    return np.sum(energy_array)


def main(N=4, T=5, ntimesteps=10**2, nHsteps=50, Hmax=2):

    nsites = N**2
    total_steps = ntimesteps * nsites

    # Initialisation of lattice
    lattice = np.random.choice([1, -1], size=(N, N))
    
    # Initialise arrays
    H_arr_up = np.linspace(-Hmax, +Hmax, num=nHsteps)
    H_arr_down = np.linspace(+Hmax, -Hmax, num=nHsteps)
    M_arr_up = np.empty(nHsteps)
    M_arr_down = np.empty(nHsteps)
    
    H_ind_up = 0     # H-field loop indexing integer
    
    # H-field loop
    for H in H_arr_up:

        # Define thermodynamic observables
        m = total_magnetisation(lattice)    # magnetisation counter
        M = 0

        random_site = np.random.randint(N, size=(total_steps, 2))
        tstep_ind = 0  # timestep loop indexing integer

        # Main timestep loop
        for timestep in range(ntimesteps):

            # Do a lattice sweep
            for site in range(nsites):
                i, j = random_site[tstep_ind][0], random_site[tstep_ind][1]
                dE = energy_required_to_flip(lattice, N, i, j, H)
                if dE < 0 or np.exp(-dE / T) >= np.random.rand():
                    lattice[i][j] = -lattice[i][j]
                    m += 2 * lattice[i][j]
                # End of lattice sweep loop

            # Update thermodynamic observables
            M += m

            tstep_ind += 1
            # End of time step loop

        # Update averages
        M_av = M / total_steps

        # Place obseravables into arrays
        M_arr_up[H_ind_up] = M_av
        
        H_ind_up += 1
    
    
    H_ind_down = 0     # H-field loop indexing integer
    
    for H in H_arr_down:
        
    # Define thermodynamic observables
        m = total_magnetisation(lattice)    # magnetisation counter

        M = 0

        random_site = np.random.randint(N, size=(total_steps, 2))
        tstep_ind = 0  # timestep loop indexing integer

        # Main timestep loop
        for timestep in range(ntimesteps):

            # Do a lattice sweep
            for site in range(nsites):
                i, j = random_site[tstep_ind][0], random_site[tstep_ind][1]
                dE = energy_required_to_flip(lattice, N, i, j, H)
                if dE < 0 or np.exp(-dE / T) >= np.random.rand():
                    lattice[i][j] = -lattice[i][j]
                    m += 2 * lattice[i][j]
                # End of lattice sweep loop

            # Update thermodynamic observables
            M += m

            tstep_ind += 1
            # End of time step loop

        # Update averages
        M_av = M / total_steps

        # Place obseravables into arrays
        M_arr_down[H_ind_down] = M_av
            
            
        H_ind_down += 1
        # end of H-field loop

    out = np.vstack((H_arr_up, M_arr_up, M_arr_down)).T
    
    return out
