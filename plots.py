import numpy as np
import matplotlib.pyplot as plt

# Load data from files
N12 = np.loadtxt('data/N12+').T
N10 = np.loadtxt('data/N10+').T
N8 = np.loadtxt('N8').T
N6 = np.loadtxt('data/N6+').T
N4 = np.loadtxt('data/N4+').T

# X-axis for plots
T_c = 2 / np.log(1 + np.sqrt(2))
T = np.linspace(1, 5, num=50)
t = T / T_c

# |Magnetisation| per spin
plt.figure()
plt.plot(t, N12[6], '.', label='$N=12$')
plt.plot(t, N10[6], '.', label='$N=10$')
plt.plot(t, N8[1], '.', label='$N=8$')
plt.plot(t, N6[6], '.', label='$N=6$')
plt.plot(t, N4[6], '.', label='$N=4$')
plt.xlabel('$T/T_c$')
plt.ylabel('$|M|$')
plt.title('|Magnetisation| per spin')
plt.legend()

# Energy per spin
plt.figure()
plt.plot(t, N12[2], '.', label='$N=12$')
plt.plot(t, N10[2], '.', label='$N=10$')
plt.plot(t, N8[2], '.', label='$N=8$')
plt.plot(t, N6[2], '.', label='$N=6$')
plt.plot(t, N4[2], '.', label='$N=4$')
plt.xlabel('$T/T_c$')
plt.ylabel('$E$')
plt.title('Energy per spin')
plt.legend()

# Susceptibility per spin
plt.figure()
plt.plot(t, N12[7], '.', label='$N=12$')
plt.plot(t, N10[7], '.', label='$N=10$')
plt.plot(t, N8[3], '.', label='$N=8$')
plt.plot(t, N6[7], '.', label='$N=6$')
plt.plot(t, N4[7], '.', label='$N=4$')
plt.xlabel('$T/T_c$')
plt.ylabel('$\chi$')
plt.title('Susceptibility per spin')
plt.legend()

# Heat Capcity per spin
plt.figure()
plt.plot(t, N12[4], '.', label='$N=12$')
plt.plot(t, N10[4], '.', label='$N=10$')
plt.plot(t, N8[4], '.', label='$N=8$')
plt.plot(t, N6[4], '.', label='$N=6$')
plt.plot(t, N4[4], '.', label='$N=4$')
plt.xlabel('$T/T_c$')
plt.ylabel('$C$')
plt.title('Heat Capacity per spin')
plt.legend()
