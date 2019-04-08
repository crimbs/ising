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
N8 = np.loadtxt('N8+').T
N6 = np.loadtxt('N6+').T
N4 = np.loadtxt('N4+').T
#N2 = np.loadtxt('N2+').T

N_arr = np.array([4, 6, 8, 10, 12])
xdata = np.log(N_arr)

Xmax12 = N12[4][np.argmax(N12[4])]
Xmax10 = N10[4][np.argmax(N10[4])]
Xmax8 = N8[4][np.argmax(N8[4])]
Xmax6 = N6[4][np.argmax(N6[4])]
Xmax4 = N4[4][np.argmax(N4[4])]
#Xmax2 = N2[4][np.argmax(N2[4])]
Xmax_arr = np.array([Xmax4, Xmax6, Xmax8, Xmax10, Xmax12])
ydata = Xmax_arr

popt, pcov = optimize.curve_fit(line, xdata, ydata)

alpha = nu * popt[0]

plt.figure()
plt.plot(xdata, ydata, 'o', label='data')
#plt.errorbar(xdata, ydata, yerr=0.08)
plt.plot(
    np.linspace(
        0, 3), line(
            np.linspace(
                0, 3), *popt), 'b--', label='fit: alpha=%5.3f' % alpha)
plt.xlabel('$Ln(L)$')
plt.ylabel('$C_{max}$')
plt.xlim(0, 3)
plt.legend()