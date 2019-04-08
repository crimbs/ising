import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# Heat capacity

alpha = np.log(0.7)
nu = 0.9


def scaling_factor(N): 
    return N**(alpha / nu)

up = 50
down = 50

T_c = 2 / np.log(1 + np.sqrt(2))
T = np.linspace(1, 5, num=50)
Tnew = np.linspace(1, 5, num=up)
t = (T_c - T) / T_c
tnew = (Tnew - T_c) / T_c

N16 = np.loadtxt('N16').T
N10 = np.loadtxt('N10+').T
N8 = np.loadtxt('N8+').T
N6 = np.loadtxt('N6+').T
N4 = np.loadtxt('N4+').T
N2 = np.loadtxt('N2+').T

plt.figure()
#plt.plot(t, N16[4], '.', label='$N=16$')
plt.plot(tnew, scaling_factor(10)*signal.resample_poly(N10[4], up, down), label='$N=10$')
plt.plot(tnew, scaling_factor(8)*signal.resample_poly(N8[4], up, down), label='$N=8$')
plt.plot(tnew, scaling_factor(6)*signal.resample_poly(N6[4], up, down), label='$N=6$')
#plt.plot(tnew, scaling_factor(4)*signal.resample_poly(N4[4], up, down), label='$N=4$')
#plt.plot(t, N2[4], '.', label='$N=2$')
plt.xlabel('Reduced Temperature $t$')
plt.ylabel('Heat capacity scaling function')
plt.title('Heat Capacity per spin')
plt.legend()