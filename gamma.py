from matplotlib2tikz import save as tikz_save
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


def line(x, m, c):
    return (m * x) + c


def estimate_Tc(x):
    return np.argmax(x[7])


nu = 1
T_c = 2 / np.log(1 + np.sqrt(2))

N12 = np.loadtxt('N12+').T
N10 = np.loadtxt('N10+').T
#N8 = np.loadtxt('N8').T
N6 = np.loadtxt('N6+').T
N4 = np.loadtxt('N4+').T
#N2 = np.loadtxt('N2+').T

N_arr = np.array([4, 6, 10, 12])
xdata = np.log(N_arr)

Xmax12 = N12[7][np.argmax(N12[7])]
Xmax10 = N10[7][np.argmax(N10[7])]
#Xmax8 = N8[7][np.argmax(N8[7])]
Xmax6 = N6[7][np.argmax(N6[7])]
Xmax4 = N4[7][np.argmax(N4[7])]
#Xmax2 = N2[7][np.argmax(N2[7])]
Xmax_arr = np.array([Xmax4, Xmax6, Xmax10, Xmax12])
ydata = np.log(Xmax_arr)

popt, pcov = optimize.curve_fit(line, xdata, ydata)

gamma = nu * popt[0]


plt.figure()
plt.errorbar(xdata, ydata, yerr=0.5, label='data')
#plt.errorbar(xdata, ydata, yerr=0.08)
plt.plot(
    np.linspace(
        0, 3), line(
            np.linspace(
                0, 3), *popt), 'b--', label='fit: gamma=%5.3f' %
    gamma)
plt.xlabel('$Ln(L)$')
plt.ylabel(r'$\ln(\chi_{max})$')
plt.xlim(0, 3)
plt.legend()

tikz_save('gam.tex')
