import numpy as np
import time
# Define global variables
N = 4                           # N x N lattice sites

# Initialisation of lattice
lattice = np.random.choice([1, -1], size=(N, N))

       
def energy(lattice):
    return -1 * lattice * (np.roll(lattice, -1, 0)
                           + np.roll(lattice, +1, 0)
                           + np.roll(lattice, -1, 1)
                           + np.roll(lattice, +1, 1))
    
def M(lattice):
    return np.sum(lattice)

def M_av(lattice):
    return np.mean(lattice)

def E(lattice):
    return np.sum(energy(lattice))

def E_av(lattice):
    return np.mean(energy(lattice))

def energy_of_site(lattice, i, j):
    return -1 * lattice[i, j] * (lattice[((i - 1) % N), j]
                                 + lattice[((i + 1) % N), j]
                                 + lattice[i, ((j - 1) % N)]
                                 + lattice[i, ((j + 1) % N)])

i = 1,1
lattic = np.random.choice([1, -1], size=(N, N))
testo = energy_of_site(lattic, *i)

#T_array = np.linspace(0.0001,6,num=20)

#test = np.array([mag_temp(t) for t in T_array])
#west = np.array([mag_temp(t) for t in T_array])

#plt.figure()
#plt.plot(T_array,test,'.')
#plt.plot(T_array,west,'.')
#from matplotlib2tikz import save as tikz_save
#tikz_save('crit_temp.tex', figurewidth='\linewidth')

bigness = 10**4

oneway = np.random.rand(10)

def anotherway():
    for i in range(bigness):
        return (np.random.rand())

