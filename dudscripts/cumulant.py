import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N16 = np.loadtxt('N16+').T
N10 = np.loadtxt('N10+').T
N8 = np.loadtxt('N8+').T
N6 = np.loadtxt('N6+').T
N4 = np.loadtxt('N4+').T
N2 = np.loadtxt('N2+').T

up = 80
down = 50

T_c = 2 / np.log(1 + np.sqrt(2))
T = np.linspace(1, 5, num=50)
t = T / T_c
Tnew = np.linspace(1, 5, num=up)
tnew = Tnew / T_c

plt.figure()
plt.plot(t, np.abs(N16[5]), '.', label='$N=16$')
plt.plot(t, np.abs(N10[5]), '.', label='$N=10$')
plt.plot(t, np.abs(N8[5]), '.', label='$N=8$')
plt.plot(t, np.abs(N6[5]), '.', label='$N=6$')
plt.plot(t, np.abs(N4[5]), '.', label='$N=4$')
plt.plot(t, np.abs(N2[5]), '.', label='$N=2$')
plt.xlabel('$T/T_c$')
plt.ylabel('$U$')
plt.title('Cumulant')
plt.legend()
