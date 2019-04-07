import numpy as np
import matplotlib.pyplot as plt

N16 = np.loadtxt('N16').T
N8 = np.loadtxt('N8+').T
N4 = np.loadtxt('N4+').T
N2 = np.loadtxt('N2+').T

T_c = 2 / np.log(1 + np.sqrt(2))
T = np.linspace(1, 5, num=50)
t = T / T_c

plt.figure()
#plt.plot(t, np.abs(N16[1]), '.', label='$N=16$')
plt.plot(t, np.abs(N8[1]), '.', label='$N=8$')
plt.plot(t, np.abs(N4[1]), '.', label='$N=4$')
plt.plot(t, np.abs(N2[1]), '.', label='$N=2$')
plt.xlabel('$T$')
plt.ylabel('$M$')
plt.title('Magnetisation per spin')
plt.legend()

plt.figure()
#plt.plot(t, N16[2], '.', label='$N=16$')
plt.plot(t, N8[2], '.', label='$N=8$')
plt.plot(t, N4[2], '.', label='$N=4$')
plt.plot(t, N2[2], '.', label='$N=2$')
plt.xlabel('$T$')
plt.ylabel('$E$')
plt.title('Energy per spin')
plt.legend()

plt.figure()
#plt.plot(t, N16[3], '.', label='$N=16$')
plt.plot(t, N8[3], '.', label='$N=8$')
plt.plot(t, N4[3], '.', label='$N=4$')
plt.plot(t, N2[3], '.', label='$N=2$')
plt.xlabel('$T$')
plt.ylabel('$\chi$')
plt.title('Susceptibility per spin')
plt.legend()

plt.figure()
#plt.plot(t, N16[4], '.', label='$N=16$')
plt.plot(t, N8[4], '.', label='$N=8$')
plt.plot(t, N4[4], '.', label='$N=4$')
plt.plot(t, N2[4], '.', label='$N=2$')
plt.xlabel('$T$')
plt.ylabel('$C$')
plt.title('Heat Capacity per spin')
plt.legend()

plt.figure()
#plt.plot(t, N16[5], '.', label='$N=16$')
plt.plot(t, N8[5], '.', label='$N=8$')
plt.plot(t, N4[5], '.', label='$N=4$')
plt.plot(t, N2[5], '.', label='$N=2$')
plt.xlabel('$T$')
plt.ylabel('$U$')
plt.title('Cumulant')
plt.legend()

plt.figure()
#plt.plot(t, np.abs(N16[6]), '.', label='$N=16$')
#plt.plot(t, np.abs(N8[6]), '.', label='$N=8$')
plt.plot(t, np.abs(N4[6]), '.', label='$N=4$')
plt.plot(t, np.abs(N2[6]), '.', label='$N=2$')
plt.xlabel('$T$')
plt.ylabel('$|M|$')
plt.title('|Magnetisation| per spin')
plt.legend()

plt.figure()
#plt.plot(t, np.abs(N16[7]), '.', label='$N=16$')
#plt.plot(t, np.abs(N8[7]), '.', label='$N=8$')
plt.plot(t, np.abs(N4[7]), '.', label='$N=4$')
plt.plot(t, np.abs(N2[7]), '.', label='$N=2$')
plt.xlabel('$T$')
plt.ylabel('$\chi$ using $|M|$')
plt.title('Susceptibility using $|M|$ per spin')
plt.legend()
