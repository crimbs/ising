import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize

# Load data
N64 = np.loadtxt('data/N64').T
N32 = np.loadtxt('data/N32').T
N16 = np.loadtxt('data/N16').T
N8 = np.loadtxt('data/N8').T
N4 = np.loadtxt('data/N4').T


def line(x, m, c):
    return (m * x) + c


def estimate_Tc(x):
    return x[0][np.argmax(x[3])]


# Global variables
nu = 0.95
T_c = 2 / np.log(1 + np.sqrt(2))

# N array
N_arr = np.array([4, 8, 16, 32, 64])
xdata = np.power(N_arr, -1 / nu)

#-----------------------T_c-----------------------#

Tc64 = estimate_Tc(N64)
Tc32 = estimate_Tc(N32)
Tc16 = estimate_Tc(N16)
Tc8 = estimate_Tc(N8)
Tc4 = estimate_Tc(N4)
ydata = np.array([Tc4, Tc8, Tc16, Tc32, Tc64])

horiz = np.linspace(0, 0.3)

# Main plot
popt, pcov = optimize.curve_fit(line, xdata, ydata)
plt.errorbar(xdata, ydata, yerr=0.04, elinewidth=0)
plt.plot(horiz, line(horiz, *popt), 'g-', 
                             label='fit: a=%5.3f, $T_c$=%5.3f' %tuple(popt))

# Maximum slope
popt, pcov = optimize.curve_fit(line, np.array([xdata[0], xdata[4]]), 
                                    np.array([ydata[0]+0.04, ydata[4]-0.04]))
plt.plot(horiz, line(horiz, *popt), 'r--', 
                             label='max: a=%5.3f, $T_c$=%5.3f' %tuple(popt))

# Minimum slope
popt, pcov = optimize.curve_fit(line, np.array([xdata[0], xdata[4]]), 
                                    np.array([ydata[0]-0.04, ydata[4]+0.04]))
plt.plot(horiz, line(horiz, *popt), 'r--', 
                             label='min: a=%5.3f, $T_c$=%5.3f' %tuple(popt))

plt.xlabel('$N^{1/v}$')
plt.ylabel('$T_{c}(N)$')
plt.xlim(0,0.3)
plt.ylim(2,3)
plt.tight_layout()
plt.legend()

#-----------------------C_0-----------------------#

Cmax64 = N64[4].max()
Cmax32 = N32[4].max()
Cmax16 = N16[4].max()
Cmax8 = N8[4].max()
Cmax4 = N4[4].max()
Cmax_arr = np.array([Cmax4, Cmax8, Cmax16, Cmax32, Cmax64])
ydata = Cmax_arr
xdata = np.log(N_arr)

popt, pcov = optimize.curve_fit(line, xdata, ydata)

alpha = nu * popt[0]

plt.figure()
plt.errorbar(xdata, ydata, yerr=0.03)
plt.plot(np.linspace(0, 5), line(np.linspace(0, 5), *popt), 'b--', 
                                         label='alpha=%5.3f' % alpha)
plt.xlabel('$Ln(N)$')
plt.ylabel('$C_{max}$')
plt.xlim(0, 5)
plt.legend()

#-----------------------Beta-----------------------#

T = np.linspace(1, 5, num=50)
x = np.log((T_c - T) / T_c)
y = np.log(N32[1])

popt, pcov = optimize.curve_fit(line, x[13:15], y[13:15])

plt.figure()
plt.plot(x, y, '.')
plt.plot(np.linspace(-4, 0.2), line(np.linspace(-4, 0.2), 0.125, 0.19), 'g--', 
                                                     label='beta=%5.3f' % 0.125)
plt.ylim(-0.35,0.05)
plt.xlim(-4,-0.5)
plt.xlabel('$Ln((T_{c} - T) / T_{c})$')
plt.ylabel('$Ln(|M|)$')
plt.legend()
from matplotlib2tikz import save as tikz_save
tikz_save('bet.tex')

#-----------------------Gamma-----------------------#

Xmax64 = N64[3].max()
Xmax32 = N32[3].max()
Xmax16 = N16[3].max()
Xmax8 = N8[3].max()
Xmax4 = N4[3].max()
Xmax_arr = np.array([Xmax4, Xmax8, Xmax16, Xmax32, Xmax64])
ydata = np.log(Xmax_arr)

popt, pcov = optimize.curve_fit(line, xdata, ydata)

gamma = nu * popt[0]

plt.figure()
plt.errorbar(xdata, ydata, yerr=0.5)
plt.plot(np.linspace(0, 5), line(np.linspace(0, 5), *popt), 'b--', 
                                         label='gamma=%5.3f' % gamma)
plt.xlabel('$Ln(N)$')
plt.ylabel(r'$\ln(\chi_{max})$')
plt.xlim(0, 5)
plt.legend()

#-----------------------Nu-----------------------#

T = np.linspace(1, 5, num=50)
x = np.log((T - T_c) / T_c)
y = np.log(N64[5])
popt, pcov = optimize.curve_fit(line, x[43:49], y[43:49])

nu = -popt[0]

plt.figure()
plt.plot(x, y, '.')
plt.plot(np.linspace(-4, 0.2), line(np.linspace(-4, 0.2), *popt), 'b--', 
                                                     label='nu=%5.3f' % nu)
plt.ylim(-1.5,0)
#plt.xlim(-4,-0.5)
#plt.xlabel('$Ln((T_{c} - T) / T_{c})$')
#plt.ylabel('$Ln(|M|)$')
plt.legend()

#-----------------------Nu2-----------------------#

ximax64 = np.abs(np.gradient(N64[5])).max()
ximax32 = np.abs(np.gradient(N32[5])).max()
ximax16 = np.abs(np.gradient(N16[5])).max()
ximax8 = np.abs(np.gradient(N8[5])).max()
ximax4 = np.abs(np.gradient(N4[5])).max()
ximax_arr = np.array([ximax4, ximax8, ximax16, ximax32, ximax64])
ydata = np.log(ximax_arr)

popt, pcov = optimize.curve_fit(line, xdata, ydata)

nu = popt[0]

plt.figure()
plt.errorbar(xdata, ydata, yerr=0.5)
plt.plot(np.linspace(0, 5), line(np.linspace(0, 5), *popt), 'b--', 
                                         label='nu=%5.3f' % nu)
plt.plot(np.linspace(0, 5), line(np.linspace(0, 5), 1, -5.5), 'g--', 
                                         label='nu=1')
plt.xlabel('$Ln(N)$')
plt.ylabel(r'$\ln(\eta_{max})$')
plt.xlim(0, 5)
plt.legend()


#-----------------------z-----------------------#

wol = np.loadtxt('data/wolff').T
met = np.loadtxt('data/metropolis').T

xdataw = np.log(wol[0])
ydataw = np.log(wol[1])
poptw, pcovw = optimize.curve_fit(line, xdataw, ydataw)

xdatam = np.log(met[0])
ydatam = np.log(met[1])
poptm, pcovm = optimize.curve_fit(line, xdatam, ydatam)

plt.figure()
plt.plot(xdataw, ydataw, '.', label='wolff')
plt.plot(np.linspace(xdataw.min(), xdataw.max()), line(np.linspace(xdataw.min(), xdataw.max()), *poptw), 'b--', label='z_w=%5.3f ' % poptw[0])
plt.plot(xdatam, ydatam, '.', label='met')
plt.plot(np.linspace(xdatam.min(), xdatam.max()), line(np.linspace(xdatam.min(), xdatam.max()), *poptm), 'b--', label='z_m=%5.3f ' % poptm[0])
plt.legend()