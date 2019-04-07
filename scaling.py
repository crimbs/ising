import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize

nu = 1
T_c = 2 / np.log(1 + np.sqrt(2))

N8 = np.loadtxt('N8+').T
N4 = np.loadtxt('N4+').T
N2 = np.loadtxt('N2+').T

max8 = N8[0][np.argmax(N8[4])]
max4 = N4[0][np.argmax(N4[4])]
max2 = N2[0][np.argmax(N2[4])]


N_arr = np.array([2, 4, 8])
xdata = np.power(N_arr, -1/nu)
ydata = np.array([max2, max4, max8])

def func(x, m, c):
    return (m * x) + c

popt, pcov = optimize.curve_fit(func, xdata, ydata)

plt.figure()
plt.plot(xdata, ydata, 'o', label='data')
plt.plot(np.linspace(0,0.6), func(np.linspace(0,0.6), *popt), 'g--', label='fit: m=%5.3f, c=%5.3f' % tuple(popt))
plt.plot(0, T_c, 'ro', label='Onsager')
plt.xlabel('$Ln(N)$')
plt.ylabel('$Ln(C)$')
plt.title('Critical Exponent')
plt.legend()
