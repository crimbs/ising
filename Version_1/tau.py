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

    M = ising.main(N=n, T=t, nsteps=10**4, mag=True, everystep=False)
    ACF = stats.acf(M)
    out = stats.tau_e(ACF)
    return out


T_c = 2 / np.log(1 + np.sqrt(2))
T_array = np.linspace(2.5, 7, num=30)
N_array = np.array([2, 4, 8, 16])

tau = np.array([np.array([main(T=t, N=n) for t in T_array]) for n in N_array])

# tau_e vs temp plot
plt.figure()
plt.plot(T_array, tau[0], label='$N=2$')
plt.plot(T_array, tau[1], label='$N=4$')
plt.plot(T_array, tau[2], label='$N=8$')
plt.plot(T_array, tau[3], label='$N=16$')
plt.xlabel('$T$')
plt.ylabel('tau_e')
plt.legend()
plt.savefig('tau_e_vs_temp.pdf')

from matplotlib2tikz import save as tikz_save
tikz_save('filename.tex')