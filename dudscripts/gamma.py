import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# Susceptibility

gamma = 1.75
nu = 1

def scaling_factor(N): 
    return N**(-gamma / nu)

up = 25
down = 50

T_c = 2 / np.log(1 + np.sqrt(2))
T = np.linspace(1, 5, num=50)
Tnew = np.linspace(1, 5, num=up)
t = (T_c - T) / T_c
tnew = (T_c - Tnew) / T_c

N16 = np.loadtxt('N16+').T
N10 = np.loadtxt('N10+').T
N8 = np.loadtxt('N8+').T
N6 = np.loadtxt('N6+').T
N4 = np.loadtxt('N4+').T
N2 = np.loadtxt('N2+').T

plt.figure()
plt.plot(tnew, scaling_factor(16)*signal.resample_poly(N16[7], up, down), '.', label='$N=16$')
plt.plot(tnew, scaling_factor(10)*signal.resample_poly(N10[7], up, down), '.', label='$N=10$')
#plt.plot(t, np.abs(N8[7]), '.', label='$N=8$')
plt.plot(tnew, scaling_factor(6)*signal.resample_poly(N6[7], up, down), '.', label='$N=6$')
plt.plot(tnew, scaling_factor(4)*signal.resample_poly(N4[7], up, down), '.', label='$N=4$')
plt.plot(tnew, scaling_factor(2)*signal.resample_poly(N2[7], up, down), '.', label='$N=2$')
plt.xlabel('$t$')
plt.ylabel('$\chi$ using $|M|$')
plt.title('Susceptibility using $|M|$ per spin')
plt.legend()
