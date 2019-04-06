import numpy as np
import matplotlib.pyplot as plt
import ising

def main(T=5, N=4):
    """
    Returns heat capacity per spin
    """
    t = T
    n = N

    E = ising.main(N=n, T=t, nsteps=10**5, mag=False, energy= True, everystep=False)
    C = np.var(E) / (n**2 * t**2)
    return C



T_array = np.linspace(1, 5)


C = np.array([main(T=t, N=32) for t in T_array])

# plot
plt.figure()
plt.plot(T_array, C, label='$N=32$')
plt.xlabel('$T$')
plt.ylabel('$C$')
plt.legend()
plt.savefig('n32.pdf')

from matplotlib2tikz import save as tikz_save
tikz_save('n32.tex')
