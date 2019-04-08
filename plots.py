import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Load data from files
N16 = np.loadtxt('N16+').T
N12 = np.loadtxt('N12+').T
N10 = np.loadtxt('N10+').T
N8 = np.loadtxt('N8+').T
N6 = np.loadtxt('N6+').T
N4 = np.loadtxt('N4+').T
N2 = np.loadtxt('N2+').T

# Resampling factors if needed
up = 25
down = 50

# X-axis for plots
T_c = 2 / np.log(1 + np.sqrt(2))
T = np.linspace(1, 5, num=50)
t = T / T_c
Tnew = np.linspace(1, 5, num=up)
tnew = Tnew / T_c


plt.figure()
#plt.plot(t, np.abs(N16[1]), '.', label='$N=16$')
plt.plot(t, np.abs(N12[1]), '.', label='$N=12$')
plt.plot(t, np.abs(N10[1]), '.', label='$N=10$')
plt.plot(t, np.abs(N8[1]), '.', label='$N=8$')
plt.plot(t, np.abs(N6[1]), '.', label='$N=6$')
plt.plot(t, np.abs(N4[1]), '.', label='$N=4$')
#plt.plot(t, np.abs(N2[1]), '.', label='$N=2$')
plt.xlabel('$T/T_c$')
plt.ylabel('$M$')
plt.title('Magnetisation per spin')
plt.legend()

plt.figure()
#plt.plot(t, N16[2], '.', label='$N=16$')
plt.plot(t, N12[2], '.', label='$N=12$')
plt.plot(t, N10[2], '.', label='$N=10$')
plt.plot(t, N8[2], '.', label='$N=8$')
plt.plot(t, N6[2], '.', label='$N=6$')
plt.plot(t, N4[2], '.', label='$N=4$')
#plt.plot(t, N2[2], '.', label='$N=2$')
plt.xlabel('$T/T_c$')
plt.ylabel('$E$')
plt.title('Energy per spin')
plt.legend()

plt.figure()
#plt.plot(t, N16[3], '.', label='$N=16$')
plt.plot(t, N12[3], '.', label='$N=12$')
plt.plot(t, N10[3], '.', label='$N=10$')
plt.plot(t, N8[3], '.', label='$N=8$')
plt.plot(t, N6[3], '.', label='$N=6$')
plt.plot(t, N4[3], '.', label='$N=4$')
plt.plot(t, N2[3], '.', label='$N=2$')
plt.xlabel('$T/T_c$')
plt.ylabel('$\chi$')
plt.title('Susceptibility per spin')
plt.legend()

plt.figure()
#plt.plot(tnew, signal.resample_poly(N16[4], up, down), '.', label='$N=16$')
plt.plot(tnew, signal.resample_poly(N12[4], up, down), '.', label='$N=12$')
plt.plot(tnew, signal.resample_poly(N10[4], up, down), '.', label='$N=10$')
plt.plot(tnew, signal.resample_poly(N8[4], up, down), '.', label='$N=8$')
plt.plot(tnew, signal.resample_poly(N6[4], up, down), '.', label='$N=6$')
plt.plot(tnew, signal.resample_poly(N4[4], up, down), '.', label='$N=4$')
#plt.plot(t, N2[4], '.', label='$N=2$')
plt.xlabel('$T/T_c$')
plt.ylabel('$C$')
plt.title('Heat Capacity per spin')
plt.legend()

plt.figure()
#plt.plot(t, N16[5], '.', label='$N=16$')
plt.plot(t, N12[5], '.', label='$N=12$')
plt.plot(t, N10[5], '.', label='$N=10$')
plt.plot(t, N8[5], '.', label='$N=8$')
plt.plot(t, N6[5], '.', label='$N=6$')
plt.plot(t, N4[5], '.', label='$N=4$')
plt.plot(t, N2[5], '.', label='$N=2$')
plt.xlabel('$T/T_c$')
plt.ylabel('$U$')
plt.title('Cumulant')
plt.legend()

plt.figure()
#plt.plot(t, N16[6], '.', label='$N=16$')
plt.plot(t, N12[6], '.', label='$N=12$')
plt.plot(t, N10[6], '.', label='$N=10$')
#plt.plot(t, N8[6], '.', label='$N=8$')
plt.plot(t, N6[6], '.', label='$N=6$')
plt.plot(t, N4[6], '.', label='$N=4$')
#plt.plot(t, N2[6], '.', label='$N=2$')
plt.xlabel('$T/T_c$')
plt.ylabel('$|M|$')
plt.title('|Magnetisation| per spin')
plt.legend()

plt.figure()
#plt.loglog(1-t, N16[6], '.', label='$N=16$')
plt.loglog(1-t, N12[6], '.', label='$N=12$')
plt.loglog(1-t, N10[6], '.', label='$N=10$')
#plt.loglog(1-t, N8[6], '.', label='$N=8$')
#plt.loglog(1-t, N6[6], '.', label='$N=6$')
#plt.loglog(1-t, N4[6], '.', label='$N=4$')
#plt.plot(t, N2[6], '.', label='$N=2$')
plt.xlabel('$T/T_c$')
plt.ylabel('$|M|$')
plt.ylim(0.6,1)
plt.title('|Magnetisation| per spin')
plt.legend()

plt.figure()
plt.plot(tnew, signal.resample_poly(N16[7], up, down), '.', label='$N=16$')
plt.plot(tnew, signal.resample_poly(N12[7], up, down), '.', label='$N=12$')
plt.plot(tnew, signal.resample_poly(N10[7], up, down), '.', label='$N=10$')
#plt.plot(t, np.abs(N8[7]), '.', label='$N=8$')
plt.plot(tnew, signal.resample_poly(N6[7], up, down), '.', label='$N=6$')
plt.plot(tnew, signal.resample_poly(N4[7], up, down), '.', label='$N=4$')
plt.plot(tnew, signal.resample_poly(N2[7], up, down), '.', label='$N=2$')
plt.xlabel('$T/T_c$')
plt.ylabel('$\chi$ using $|M|$')
plt.title('Susceptibility using $|M|$ per spin')
plt.legend()
