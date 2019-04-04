import numpy as np
import matplotlib.pyplot as plt
import ising

def main(T=5, N=4):
    """
    Returns heat capacity per spin
    """
    t = T
    n = N

    E = ising.main(N=n, T=t, nsteps=10**4, mag=False, energy= True, everystep=False)
    C = np.var(E) / (n**2 * t**2)
    return C


T_c = 2 / np.log(1 + np.sqrt(2))
T_array = np.linspace(0.5, 5)
N_array = np.array([2, 4, 8, 16])

C = np.array([np.array([main(T=t, N=n) for t in T_array]) for n in N_array])

# plot
plt.figure()
plt.plot(T_array, C[0], label='$N=2$')
plt.plot(T_array, C[1], label='$N=4$')
plt.plot(T_array, C[2], label='$N=8$')
plt.plot(T_array, C[3], label='$N=16$')
plt.xlabel('$T$')
plt.ylabel('$C$')
plt.legend()
plt.savefig('heatcapacity.pdf')

from matplotlib2tikz import save as tikz_save
tikz_save('filename.tex')
