import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import ising

'''
M = ising.main(N=4, T=2.5, nsteps=10**4, mag=True)[0::2]

fourth = stats.moment(M, 4)
fourth0 = stats.kstat(M, 4)

second = stats.moment(M, 2)
second0 = stats.kstat(M, 2)

U = 1 - fourth / (3 * second)
'''
def U(N=4, T=4):
    
    n = N
    t = T
    
    M = ising.main(N=n, T=t, nsteps=10**3, mag=True, energy=False, everystep=False)

    fourth = stats.moment(M, 4)

    second = stats.moment(M, 2)

    U = 1 - fourth / (3 * second)
    
    return U

T_array = np.linspace(2.5, 2.7, num=5)
N_array = np.array([32, 16, 8, 4])

cumulant = np.array([np.array([U(N=n, T=t) for t in T_array]) for n in N_array])

# plot
plt.figure()
plt.plot(T_array, cumulant[0], label='$N=32$')
plt.plot(T_array, cumulant[1], label='$N=16$')
plt.plot(T_array, cumulant[2], label='$N=8$')
plt.plot(T_array, cumulant[3], label='$N=4$')
plt.xlabel('$T$')
plt.ylabel('$U$')
plt.legend()
plt.savefig('cumulant.pdf')

from matplotlib2tikz import save as tikz_save
tikz_save('cumulant.tex')
