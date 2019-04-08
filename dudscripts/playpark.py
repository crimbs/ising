import numpy as np
import ising
import ising_old
import time
'''
start = time.time()
test = ising.main(N=4, ntimesteps=10**3, Tmin=1, Tmax=5, ntemp=20).T
C = test[4]
print(time.time() - start)

start = time.time()
def main(T=5, N=4):
    """
    Returns heat capacity per spin
    """
    t = T
    n = N

    E = ising_old.main(N=n, T=t, nsteps=10**3, mag=False, energy=True, everystep=True)
    C = np.var(E) / (n**2 * t**2)
    return C

T = np.linspace(1, 5, num=20)

C_old = np.array([main(T=t, N=4) for t in T])
print(time.time() - start)


from scipy import signal
Tre = np.linspace(1,5,num=500)
C_re = signal.resample_poly(C, up=500, down=len(T))
C_old_re = signal.resample_poly(C_old, up=500, down=len(T))


from scipy import interpolate
f_old = interpolate.interp1d(T, C_old)
f = interpolate.interp1d(T, C)
Tint = np.linspace(1, 5, num=100)


import matplotlib.pyplot as plt
plt.figure()
plt.plot(T, C_old, label='old')
plt.plot(T, C, label='new')
plt.plot(Tint, f_old(Tint), label='old inter')
plt.plot(Tint, f(Tint), label='new inter')
plt.plot(Tre, C_re, label='old resamp')
plt.plot(Tre, C_old_re, label='new resamp')
plt.legend()
plt.savefig('intvsresamp.pdf')
'''
'''
test = ising.main(N=8, ntimesteps=10**5, Tmin=1, Tmax=5, ntemp=1).T

whatis = test[6]
'''
import noburn
start = time.time()
test = noburn.main(N=4, ntimesteps=10**5, Tmin=1, Tmax=5, ntemp=1)
print(time.time() - start)





    