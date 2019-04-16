import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


def line(x, m, c):
    return (m * x) + c


def estimate_Tc(x):
    return x[0][np.argmax(x[3])]


# Load data
N32 = np.loadtxt('data/N32').T
N16 = np.loadtxt('data/N16').T
N8 = np.loadtxt('data/N8').T
N4 = np.loadtxt('data/N4').T

# Global variables
nu = 1
T_c = 2 / np.log(1 + np.sqrt(2))

# N array
N_arr = np.array([4, 8, 16, 32])
xdata = np.power(N_arr, -1 / nu)

#-----------------------T_c estimate-----------------------#

Tc32 = estimate_Tc(N32)
Tc16 = estimate_Tc(N16)
Tc8 = estimate_Tc(N8)
Tc4 = estimate_Tc(N4)
ydata = np.array([Tc4, Tc8, Tc16, Tc32])

horiz = np.linspace(0, 0.3)

# Main plot
popt, pcov = optimize.curve_fit(line, xdata, ydata)
plt.errorbar(xdata, ydata, yerr=0.04, elinewidth=0)
plt.plot(horiz, line(horiz, *popt), 'g-', 
                             label='fit: a=%5.3f, $T_c$=%5.3f' %tuple(popt))

# Maximum slope
popt, pcov = optimize.curve_fit(line, np.array([xdata[0], xdata[3]]), 
                                    np.array([ydata[0]+0.04, ydata[3]-0.04]))
plt.plot(horiz, line(horiz, *popt), 'r--', 
                             label='max: a=%5.3f, $T_c$=%5.3f' %tuple(popt))

# Minimum slope
popt, pcov = optimize.curve_fit(line, np.array([xdata[0], xdata[3]]), 
                                    np.array([ydata[0]-0.04, ydata[3]+0.04]))
plt.plot(horiz, line(horiz, *popt), 'r--', 
                             label='min: a=%5.3f, $T_c$=%5.3f' %tuple(popt))

plt.xlabel('$N^{1/v}$')
plt.ylabel('$T_{c}(N)$')
plt.xlim(0,0.3)
plt.ylim(2,3)
plt.tight_layout()
plt.legend()


#-----------------------Alpha estimate-----------------------#

Cmax32 = N32[4].max()
Cmax16 = N16[4].max()
Cmax8 = N8[4].max()
Cmax4 = N4[4].max()
Cmax_arr = np.array([Cmax4, Cmax8, Cmax16, Cmax32])
ydata = Cmax_arr
xdata = np.log(N_arr)

popt, pcov = optimize.curve_fit(line, xdata, ydata)

alpha = nu * popt[0]

plt.figure()
plt.errorbar(xdata, ydata, yerr=0.08)
plt.plot(np.linspace(0, 4), line(np.linspace(0, 4), *popt), 'b--', 
                                         label='alpha=%5.3f' % alpha)
plt.xlabel('$Ln(L)$')
plt.ylabel('$C_{max}$')
plt.xlim(0, 4)
plt.legend()


#-----------------------Beta estimate-----------------------#

T = np.linspace(1, 5, num=50)
x = np.log((T_c - T) / T_c)
y = np.log(N32[1])
plt.figure()
plt.plot(x, y, '.')
plt.plot(np.linspace(-4,-0.5), (1/8)*np.linspace(-4,-0.5)+0.18)
plt.ylim(-0.35,0.05)
plt.xlim(-4,-0.5)
plt.xlabel('$Ln((T_{c} - T) / T_{c})$')
plt.ylabel('$Ln(|M|)$')


#-----------------------Gamma estimate-----------------------#

Xmax32 = N32[3].max()
Xmax16 = N16[3].max()
Xmax8 = N8[3].max()
Xmax4 = N4[3].max()
Xmax_arr = np.array([Xmax4, Xmax8, Xmax16, Xmax32])
ydata = np.log(Xmax_arr)

popt, pcov = optimize.curve_fit(line, xdata, ydata)

gamma = nu * popt[0]

plt.figure()
plt.errorbar(xdata, ydata, yerr=0.5)
plt.plot(np.linspace(0, 4), line(np.linspace(0, 4), *popt), 'b--', 
                                         label='gamma=%5.3f' % gamma)
plt.xlabel('$Ln(L)$')
plt.ylabel(r'$\ln(\chi_{max})$')
plt.xlim(0, 4)
plt.legend()