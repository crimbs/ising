# author: Christian Hines
# date: March 2019
# tester.py
import numpy as np
from ising_class import Ising
import time
import matplotlib.pyplot as plt
start = time.time()

def metropolis_scaler(i):
    return Ising(N=4,num_steps=10**3,T=i).magnetisation()
vmetropolis = np.vectorize(metropolis_scaler)

T_array = np.linspace(0.0001,6,num=20)

y = vmetropolis(T_array)


plt.plot(T_array,y,'o')

end = time.time()
print(end - start)