import numpy as np
import time

__all__ = ['energy_required_to_flip', 
           'total_magnetisation', 
           'total_energy',
           'main']

def energy_required_to_flip(lattice, N, i, j, H):
    """
    Returns energy required to flip the spin of an 
    individual spin site (i, j) and external field H. 
    Toroidal periodic boundary conditions are imposed.
    """
    lat = np.array(lattice)
    energy_of_site = -1 * lat[i][j] * (lat[((i - 1) % N)][j]
                                       + lat[((i + 1) % N)][j]
                                       + lat[i][((j - 1) % N)]
                                       + lat[i][((j + 1) % N)]
                                       + H)
    dE = -2 * energy_of_site
    return dE


def total_magnetisation(lattice):
    """
    Returns total magnetisation of a given lattice
    """
    return np.sum(lattice)


def total_energy(lattice, H):
    """
    Returns total energy of a given lattice and external field H. 
    Toroidal periodic boundary conditions are imposed.
    """
    energy_array = -1 * lattice * (np.roll(lattice, -1, 0)
                                   + np.roll(lattice, +1, 0)
                                   + np.roll(lattice, -1, 1)
                                   + np.roll(lattice, +1, 1)
                                   + H)
    return np.sum(energy_array)


def main(N=4, T=2, ntimesteps=10**3, nHsteps=50, Hmax=2):
    """
    Function which implements the Metropolis algorithm, performing 
    a looped cycle over external field H values. The following are
    saved into a .txt file under the name 'T<temperature>.txt' (e.g. T1.txt)
    - External Field H
    - Absolute Magnetisation per spin on the upwards loop
    - Absolute Magnetisation per spin on the downwards loop
    -----------------------------
    Parameters
    -----------------------------
    N :             Lattice size (i.e. N x N lattice)
    ntimesteps :    Number of time steps (i.e. sweeps of the lattice)
    nHsteps :       Number of steps in the H loop
    Hmax :          Maximum and minimum H value bounding the loop
    """
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
                tstep_ind += 1
                # End of lattice sweep loop

            # Update thermodynamic observables
            M += m

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
                tstep_ind += 1
                # End of lattice sweep loop

            # Update thermodynamic observables
            M += m

        # Update averages
        M_av = M / total_steps

        # Place obseravables into arrays
        M_arr_down[H_ind_down] = M_av
                     
        H_ind_down += 1
        # end of H-field loop
      
    out = np.vstack((H_arr_up, M_arr_up, M_arr_down)).T
    
    np.savetxt('T%0.1f' % T, out, header='H, M up, M down')
    
    return out

start = time.time()

if __name__ == "__main__":
    main()
print(time.time() - start)

