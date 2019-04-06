import stats
import matplotlib.pyplot as plt
import numpy as np

save = np.loadtxt('n8nsteps10000').T

plt.figure()
plt.plot(save[0], save[1], '.')
plt.xlabel('$T$')
plt.ylabel('$M$')
plt.title('Magnetisation per spin')
plt.savefig('Magnetisation_per_spin.pdf')

plt.figure()
plt.plot(save[0], save[2], '.')
plt.xlabel('$T$')
plt.ylabel('$E$')
plt.title('Energy per spin')
plt.savefig('Energy_per_spin.pdf')

plt.figure()
plt.plot(save[0], save[3], '.')
plt.xlabel('$T$')
plt.ylabel(r'$\chi$')
plt.title('Susceptibility per spin')
plt.savefig('Susceptibility_per_spin.pdf')

plt.figure()
plt.plot(save[0], save[4], '.')
plt.xlabel('$T$')
plt.ylabel('$C$')
plt.title('Heat Capacity per spin')
plt.savefig('Heat_capacity_per_spin.pdf')

plt.figure()
plt.plot(save[0], save[5], '.')
plt.xlabel('$T$')
plt.ylabel('$U$')
plt.title('Cumulant')
plt.savefig('Cumulant.pdf')

M = save[0]
autocorr = stats.acf(M)
tau = stats.tau_e(autocorr)
