# author: Christian Hines
# date: March 2019
# tester.py
import numpy as np
from ising_class import Ising
import time
import matplotlib.pyplot as plt
start = time.time()

def metropolis_scaler(i):
    return Ising(T=i).magnetisation()
vmetropolis = np.vectorize(metropolis_scaler)

T_array = np.linspace(0.001,10,num=20)

y = vmetropolis(T_array)

plt.plot(T_array,y)
