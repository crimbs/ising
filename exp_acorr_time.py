import numpy as np
import matplotlib.pyplot as plt
import ising
import stats


def main(T=5, N=4):
    """
    Returns tau_e as a function of temp and lattice size
    """
    t = T
    n = N

    M = ising.main(N=n, T=t, nsteps=10**3, mag=True, everystep=True)
    ACF = stats.acf(M)
    out = stats.tau_e(ACF)
    return out


T_c = 2 / np.log(1 + np.sqrt(2))
T_array = np.linspace(T_c + 0.1, 10, num=40)
N_array = np.array([4, 8, 16])

tau = np.array([np.array([main(T=t, N=n) for t in T_array]) for n in N_array])

# tau_e vs temp plot
plt.figure()
plt.plot(T_array, tau[0], label='$N=4$')
plt.plot(T_array, tau[1], label='$N=8$')
plt.plot(T_array, tau[2], label='$N=16$')
plt.xlabel('$T$')
plt.ylabel('tau_e')
plt.legend()
plt.savefig('tau_e_vs_temp.pdf')
