from matplotlib2tikz import save as tikz_save
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


def line(x, m, c):
    return (m * x) + c


N10 = np.loadtxt('N10+').T

# Data for plots
T_c = 2 / np.log(1 + np.sqrt(2))
T = np.linspace(1, 5, num=50)
t = (T_c - T) / T_c
lnt = np.log(t)
lnM = np.log(N10[6])
xdata = lnt[10:16]
ydata = lnM[10:16]

popt, pcov = optimize.curve_fit(line, xdata, ydata)

beta = popt[0]

plt.figure()
plt.plot(lnt, lnM, '.')
plt.plot(np.linspace(-4, -0.5), line(np.linspace(-4, -0.5), *popt),
         'b--', label='beta=%5.3f' % beta)
plt.xlabel(r'$\ln(T_{c}-T/T_{c})$')
plt.ylabel(r'$|\ln(M|)$')
plt.xlim(-4, -0.5)
plt.ylim(-0.4, 0)
plt.legend()
tikz_save('beta.tex')
