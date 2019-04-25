import numpy as np
import matplotlib.pyplot as plt

# Load data from files:
N64 = np.loadtxt('data/N64').T
N32 = np.loadtxt('data/N32').T
N16 = np.loadtxt('data/N16').T
N8 = np.loadtxt('data/N8').T
# Hysteresis data:
T1point5 = np.loadtxt('data/N8T1.5').T
T2 = np.loadtxt('data/N8T2').T

# X-axis for plots
T_c = 2 / np.log(1 + np.sqrt(2))
T = np.linspace(1, 5, num=50)
t = T / T_c

# |Magnetisation| per spin
plt.figure()
plt.plot(t, N64[1], '.', label='$N=64$')
plt.plot(t, N32[1], '.', label='$N=32$')
plt.plot(t, N16[1], '.', label='$N=16$')
plt.plot(t, N8[1], '.', label='$N=8$')
plt.xlabel('$T/T_c$')
plt.ylabel('$|M|$')
plt.title('|Magnetisation| per spin')
plt.legend()

# Energy per spin
plt.figure()
plt.plot(t, N64[2], '.', label='$N=64$')
plt.plot(t, N32[2], '.', label='$N=32$')
plt.plot(t, N16[2], '.', label='$N=16$')
plt.plot(t, N8[2], '.', label='$N=8$')
plt.xlabel('$T/T_c$')
plt.ylabel('$E$')
plt.title('Energy per spin')
plt.legend()

# Susceptibility per spin
plt.figure()
plt.plot(t, N64[3], '.', label='$N=64$')
plt.plot(t, N32[3], '.', label='$N=32$')
plt.plot(t, N16[3], '.', label='$N=16$')
plt.plot(t, N8[3], '.', label='$N=8$')
plt.xlabel('$T/T_c$')
plt.ylabel('$\chi$')
plt.title('Susceptibility per spin')
plt.legend()

# Heat Capcity per spin
plt.figure()
plt.plot(t, N64[4], '.', label='$N=64$')
plt.plot(t, N32[4], '.', label='$N=32$')
plt.plot(t, N16[4], '.', label='$N=16$')
plt.plot(t, N8[4], '.', label='$N=8$')
plt.xlabel('$T/T_c$')
plt.ylabel('$C$')
plt.title('Heat Capacity per spin')
plt.legend()

# Domain Size per spin
plt.figure()
plt.plot(t, N64[5], '.', label='$N=64$')
plt.plot(t, N32[5], '.', label='$N=32$')
plt.plot(t, N16[5], '.', label='$N=16$')
plt.plot(t, N8[5], '.', label='$N=8$')
plt.xlabel('$T/T_c$')
plt.ylabel('Largest Domain')
plt.title('Domain Size per spin')
plt.legend()

# Hysteresis Plot
plt.figure()
plt.plot(T1point5[0], T1point5[1])
plt.plot(T1point5[0], np.flip(T1point5[2]))
plt.plot(T2[0], T2[1])
plt.plot(T2[0], np.flip(T2[2]))
plt.xlabel('$H$')
plt.ylabel('$M$')