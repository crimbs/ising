import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.optimize as optimize


def line(x, m, c):
    return (m * x) + c


N12 = np.loadtxt('N12+').T

# Data for plots
T_c = 2 / np.log(1 + np.sqrt(2))
T = np.linspace(1, 5, num=50)
t = (T_c - T) / T_c
lnt = np.log(t)
lnM = np.log(N12[6])
xdata = lnt[14:16]
ydata = lnM[14:16]

popt, pcov = optimize.curve_fit(line, xdata, ydata)

plt.figure()
plt.plot(lnt, lnM, '.')
plt.plot(np.linspace(-4, -0.5), line(np.linspace(-4, -0.5), *popt), 'b--', label='fit: m=%5.3f, c=%5.3f' % tuple(popt))
plt.xlabel('$\ln(T_{c}-T/T_{c})$')
plt.ylabel('$|\ln(M|)$')
plt.xlim(-4, -0.5)
plt.ylim(-0.4, 0)
plt.legend()
from matplotlib2tikz import save as tikz_save
tikz_save('beta.tex')
