import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


def line(x, m, c):
    return (m * x) + c


N = np.array([4, 8, 16])

steps = np.array([28, 49, 96])

_N = np.log(N)

popt, pcov = optimize.curve_fit(line, _N, steps)

plt.figure()
plt.plot(_N, steps)
plt.plot(np.linspace(_N.min(), _N.max()), line(np.linspace(_N.min(), _N.max()), *popt), 'b--', label='fit: m=%5.3f c=%5.3f' % tuple(popt))
plt.plot(np.linspace(_N.min(), _N.max()), line(np.linspace(_N.min(), _N.max()), 48+6, -54), 'g--', label='max')
plt.plot(np.linspace(_N.min(), _N.max()), line(np.linspace(_N.min(), _N.max()), 48-6, -27), 'r--', label='min')
plt.xlabel('$N^2$')
plt.ylabel('Steps')
plt.legend()

line(12**2, 24, -780)

(55-42)/2
