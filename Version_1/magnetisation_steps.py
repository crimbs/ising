import matplotlib.pyplot as plt
import ising

M = ising.main(N=8, T=1, nsteps=100, mag=True, everystep=False, burn=False)
M1 = ising.main(N=8, T=1, nsteps=100, mag=True, everystep=False, burn=False)

# ACF plot
plt.figure()
plt.plot(range(len(M)), M)
plt.plot(range(len(M1)), M1)
plt.xlabel('steps')
plt.ylabel('$M$')
plt.xlim(0, len(M))
