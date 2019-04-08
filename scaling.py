from matplotlib2tikz import save as tikz_save
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize

# HEAT CAPACITY


def line(x, m, c):
    return (m * x) + c


def estimate_Tc(x):
    return x[0][np.argmax(x[4])]


nu = 1.1
T_c = 2 / np.log(1 + np.sqrt(2))

N12 = np.loadtxt('N12+').T
N10 = np.loadtxt('N10+').T
N8 = np.loadtxt('N8+').T
N6 = np.loadtxt('N6+').T
N4 = np.loadtxt('N4+').T
N2 = np.loadtxt('N2+').T

N_arr = np.array([2, 4, 6, 8, 10, 12])
xdata = np.power(N_arr, -1 / nu)

Tc12 = estimate_Tc(N12)
Tc10 = estimate_Tc(N10)
Tc8 = estimate_Tc(N8)
Tc6 = estimate_Tc(N6)
Tc4 = estimate_Tc(N4)
Tc2 = estimate_Tc(N2)
ydata = np.array([Tc2, Tc4, Tc6, Tc8, Tc10, Tc12])

# Main plot
popt, pcov = optimize.curve_fit(line, xdata, ydata)
plt.errorbar(xdata, ydata, yerr=0.08)
plt.plot(np.linspace(0, 1), line(np.linspace(0, 1), *popt), 'b--', 
                             label='fit: a=%5.3f, $T_c$=%5.3f' %tuple(popt))

# Maximum slope
popt, pcov = optimize.curve_fit(line, np.array([xdata[0], xdata[5]]), 
                                    np.array([ydata[0]+0.08, ydata[5]-0.08]))
plt.plot(xdata[0], ydata[0]+0.08, 'go')
plt.plot(xdata[5], ydata[5]-0.08, 'go')
plt.plot(np.linspace(0, 1), line(np.linspace(0, 1), *popt), 'g--', 
                             label='fit: a=%5.3f, $T_c$=%5.3f' %tuple(popt))

# Minimum slope
popt, pcov = optimize.curve_fit(line, np.array([xdata[0], xdata[5]]), 
                                    np.array([ydata[0]-0.08, ydata[5]+0.08]))
plt.plot(xdata[0], ydata[0]-0.08, 'ro')
plt.plot(xdata[5], ydata[5]+0.08, 'ro')
plt.plot(np.linspace(0, 1), line(np.linspace(0, 1), *popt), 'r--', 
                             label='fit: a=%5.3f, $T_c$=%5.3f' %tuple(popt))


plt.xlabel('$N^{1/v}$')
plt.ylabel('$T_{c}(N)$')
plt.ylim(2, 3)
plt.legend()
tikz_save('filename.tex')

(0.772 - 0.389) / 2
