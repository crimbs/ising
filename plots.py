import numpy as np
import matplotlib.pyplot as plt
import time
import ising

start_alt = time.time()
test = ising.main(N=8, T=5, nsteps=10**3)[1]
test1 = ising.main1(N=8, T=5, nsteps=10**3, mag=False, energy=True)
end_alt = time.time()
print(end_alt - start_alt)

'''
plt.figure()
plt.plot(test, label='M')
plt.legend()

plt.figure()
plt.plot(test[1], label='E')
plt.legend()
'''