import numpy as np
import ising
import time
import matplotlib.pyplot as plt

def tester(N):
    n = N

    lattice = np.random.choice([1, -1], size=(n, n))
    
    start = time.time()
    test = ising.energy_using_modulo(lattice,n)
    end = time.time()
    deff = end - start
    
    start1 = time.time()
    test1 = ising.E(lattice)
    end1 = time.time()
    deff1 = end1 - start1
    
    return deff, deff1

N_arr = range(1,100)

what = np.array([tester(n) for n in N_arr]).T

modulo = what[0]

roll = what[1]

plt.figure()
plt.plot(N_arr,modulo)
plt.plot(N_arr,roll)

from matplotlib2tikz import save as tikz_save
tikz_save('modulo.tex')