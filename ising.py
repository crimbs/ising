import numpy as np


def energy_required_to_flip(lattice, N, i, j):
    '''
    Energy required to flip the spin of an individual spin site (i, j)
    '''
    lat = np.array(lattice)
    energy_of_site = -1 * lat[i][j] * (lat[((i - 1) % N)][j]
                                       + lat[((i + 1) % N)][j]
                                       + lat[i][((j - 1) % N)]
                                       + lat[i][((j + 1) % N)])
    dE = -2 * energy_of_site
    return dE


def total_magnetisation(lattice):
    '''
    Returns total magnetisation of the system
    '''
    return np.sum(lattice)


def total_energy(lattice):
    '''
    Returns total energy of the system
    '''
    energy_array = -1 * lattice * (np.roll(lattice, -1, 0)
                                   + np.roll(lattice, +1, 0)
                                   + np.roll(lattice, -1, 1)
                                   + np.roll(lattice, +1, 1))
    return np.sum(energy_array)


def main(N=4, ntimesteps=10**4, ntemp=50):

    nburn = 1000
    nsites = N**2
    total_steps = ntimesteps * nsites

    # Initialise arrays
    T_arr = np.linspace(1, 5, num=ntemp)
    M_arr = np.empty(ntemp)
    E_arr = np.empty(ntemp)
    X_arr = np.empty(ntemp)
    C_arr = np.empty(ntemp)
    U_arr = np.empty(ntemp)

    # Initialisation of lattice
    lattice = np.random.choice([1, -1], size=(N, N))

    temp_ind = 0     # temperature loop indexing integer

    # Temperature loop
    for T in T_arr:

        # Burn-in to reach equilibrium
        random_site = np.random.randint(N, size=(nburn, 2))
        for step in range(nburn):
            i, j = random_site[step][0], random_site[step][1]
            dE = energy_required_to_flip(lattice, N, i, j)
            if dE < 0 or np.exp(-dE / T) >= np.random.rand():
                lattice[i][j] = -lattice[i][j]

        # Define thermodynamic observables
        m = total_magnetisation(lattice)    # magnetisation counter
        e = total_energy(lattice)           # energy counter
        M = 0
        Msq = 0
        Mq = 0
        E = 0
        Esq = 0

        random_site = np.random.randint(N, size=(total_steps, 2))
        tstep_ind = 0  # timestep loop indexing integer

        # Main loop
        for timestep in range(ntimesteps):

            # Do a lattice sweep
            for site in range(nsites):
                i, j = random_site[tstep_ind][0], random_site[tstep_ind][1]
                dE = energy_required_to_flip(lattice, N, i, j)
                if dE < 0 or np.exp(-dE / T) >= np.random.rand():
                    lattice[i][j] = -lattice[i][j]
                    m += 2 * lattice[i][j]
                    e += 2 * dE
                # End of lattice sweep loop

            # Update thermodynamic observables
            M += m
            Msq += m**2
            Mq += m**4
            E += e / 2
            Esq += (e / 2)**2

            tstep_ind += 1
            # End of time step loop

        # Update averages
        M_av = M / total_steps
        Msq_av = Msq / total_steps
        Mq_av = Mq / total_steps
        E_av = E / total_steps
        Esq_av = Esq / total_steps

        # Place obseravables into arrays
        M_arr[temp_ind] = M_av
        E_arr[temp_ind] = E_av
        X_arr[temp_ind] = (Msq_av - ((M_av**2) * nsites)) / (T)
        C_arr[temp_ind] = (Esq_av - ((E_av**2) * nsites)) / (T**2)
        U_arr[temp_ind] = 1 - (Mq_av / (3 * Msq_av))

        temp_ind += 1
        # end of temperature loop

    # create one master array to be returned
    out = np.vstack((T_arr, M_arr, E_arr, X_arr, C_arr, U_arr)).T

    f = np.savetxt('data', out, header='T, M, E, X, C, U')

    return out


if __name__ == "__main__":
    main()
