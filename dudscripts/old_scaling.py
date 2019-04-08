import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


def line(x, m, c):
    return (m * x) + c


def abs_gradient(x):
    return np.abs(np.gradient(x))


def C_estimate_Tc(x):
    return x[0][np.argmax(x[4])]


def M_estimate_Tc(x):
    return x[0][np.argmax(abs_gradient(x[6]))]


C_nu = 1
M_nu = 1
T_c = 2 / np.log(1 + np.sqrt(2))

N10 = np.loadtxt('N10+').T
N8 = np.loadtxt('N8+').T
N6 = np.loadtxt('N6+').T
N4 = np.loadtxt('N4+').T

N_arr = np.array([4, 6, 8, 10])

# HEAT CAPACITY
C_10 = C_estimate_Tc(N10)
C_8 = C_estimate_Tc(N8)
C_6 = C_estimate_Tc(N6)
C_4 = C_estimate_Tc(N4)

C_arr = np.array([C_4, C_6, C_8, C_10])
N_arr_C = np.power(N_arr, -1/C_nu)

popt, pcov = optimize.curve_fit(line, N_arr_C, C_arr)

plt.figure()
plt.plot(N_arr_C, C_arr, 'o', label='C')
plt.errorbar(N_arr_C, C_arr, yerr=0.08)
plt.plot(np.linspace(0,1), line(np.linspace(0,1), *popt), 'b--', label='fit: a=%5.3f, $T_c$=%5.3f' % tuple(popt))
plt.plot(0, T_c, 'ro', label='Onsager')
plt.xlabel('$N^{1/\nu}$')
plt.ylabel('$T_{c}(N)$')
plt.ylim(2,3)
plt.legend()

# MAGNETISATION
M_10 = M_estimate_Tc(N10)
M_8 = M_estimate_Tc(N8)
M_6 = M_estimate_Tc(N6)
M_4 = M_estimate_Tc(N4)

M_arr = np.array([M_4, M_6, M_8, M_10])
N_arr_M = np.power(N_arr, -1/M_nu)

popt, pcov = optimize.curve_fit(line, N_arr_M, M_arr)

plt.figure()
plt.plot(N_arr_M, M_arr, 'o', label='M')
plt.errorbar(N_arr_M, M_arr, yerr=0.08)
plt.plot(np.linspace(0,1), line(np.linspace(0,1), *popt), 'g--', label='fit: a=%5.3f, $T_c$=%5.3f' % tuple(popt))
plt.plot(0, T_c, 'ro', label='Onsager')
plt.xlabel('$N^{1/\nu}$')
plt.ylabel('$T_{c}(N)$')
plt.ylim(2,3)
plt.legend()

