import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# Susceptibility

gamma = 1.75
nu = 1

def scaling_factor(N): 
    return N**(-gamma / nu)

nresample = 25

T_c = 2 / np.log(1 + np.sqrt(2))
T = np.linspace(1, 5, num=50)
Tnew = np.linspace(1, 5, num=nresample)
t = (T_c - T) / T_c
tnew = (T_c - Tnew) / T_c

N16 = np.loadtxt('N16').T
N8 = np.loadtxt('N8+').T
N4 = np.loadtxt('N4+').T
N2 = np.loadtxt('N2+').T


plt.figure()
#plt.plot(t, scaling_factor(16)*N16[7], '.', label='$N=16$')
#plt.plot(t, scaling_factor(8)*N8[7], '.', label='$N=8$')
plt.plot(tnew, scaling_factor(4)*signal.resample_poly(N4[7],nresample,len(t)), '.', label='$N=4$')
plt.plot(tnew, scaling_factor(4)*signal.resample_poly(N2[7],nresample,len(t)), '.', label='$N=2$')
plt.legend()
