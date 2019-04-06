import numpy as np
import matplotlib.pyplot as plt
import ising

def susceptibility(T, N):
    """
    Returns susceptibility per spin
    """
    t = T
    n = N

    M = ising.main(N=n, T=t, nsteps=10**4, mag=True, everystep=False)
    X = np.var(M) / (n**2 * t)
    return X


T_c = 2 / np.log(1 + np.sqrt(2))
T_array = np.linspace(1, 4)
N_array = np.array([16, 8, 4, 2])

X = np.array([np.array([susceptibility(T=t, N=n) for t in T_array]) for n in N_array])

# plot
plt.figure()
plt.plot(T_array, X[0], label='$N=16$')
plt.plot(T_array, X[1], label='$N=8$')
plt.plot(T_array, X[2], label='$N=4$')
plt.plot(T_array, X[3], label='$N=2$')
plt.xlabel('$T$')
plt.ylabel('$X$')
plt.legend()
plt.savefig('susceptibility.pdf')

from matplotlib2tikz import save as tikz_save
tikz_save('suscept.tex')
