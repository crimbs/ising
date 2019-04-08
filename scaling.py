import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize

#using heat capacity

nu = 1
T_c = 2 / np.log(1 + np.sqrt(2))

N10 = np.loadtxt('N10+').T
N8 = np.loadtxt('N8+').T
N6 = np.loadtxt('N6+').T
N4 = np.loadtxt('N4+').T
N2 = np.loadtxt('N2+').T

max10 = N10[0][np.argmax(N10[4])]
max8 = N8[0][np.argmax(N8[4])]
max6 = N6[0][np.argmax(N6[4])]
max4 = N4[0][np.argmax(N4[4])]
max2 = N2[0][np.argmax(N2[4])]


N_arr = np.array([2, 4, 6, 8, 10])
xdata = np.power(N_arr, -1/nu)
ydata = np.array([max2, max4, max6, max8, max10])

def func(x, m, c):
    return (m * x) + c

popt, pcov = optimize.curve_fit(func, xdata, ydata)

plt.figure()
plt.plot(xdata, ydata, 'o', label='data')
plt.errorbar(xdata, ydata, yerr=0.08)
plt.plot(np.linspace(0,0.6), func(np.linspace(0,0.6), *popt), 'g--', label='fit: a=%5.3f, $T_c$=%5.3f' % tuple(popt))
plt.plot(0, T_c, 'ro', label='Onsager')
plt.xlabel('$N^-1/nu$')
plt.ylabel('$T_{max}$')
plt.title('Critical Exponent')
plt.ylim(0,3)
#plt.xlim(0,0.6)
plt.legend()
from matplotlib2tikz import save as tikz_save
tikz_save('scaling.tex')
