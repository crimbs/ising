import numpy as np
import matplotlib.pyplot as plt
import magsteps
import scipy.optimize as optimize


def line(x, m, c):
    return (m * x) + c


def acf(M):
    """
    Autocorrelation for 1D array
    """
    Mdash = M - np.mean(M)
    N = len(M)
    d = N * np.ones(2 * N - 1)
    acov = (np.correlate(Mdash, Mdash, 'full') / d)[N - 1:]
    acf = acov[:N + 1] / acov[0]
    return acf


def tau_e(acf):
    """
    Returns exponential autocorrelation time tau_e
    """
    exp_factor = 1 / np.exp(1)
    tau_e = len(np.extract(acf >= exp_factor, acf))
    return tau_e


def wolff(N):
    n = N
    M = magsteps.main(N=n, ntimesteps=10**3, T=2.5, metropolis=False, 
                                                          wolff=True).T[1]
    out = tau_e(acf(M))
    return out
    
def metropolis(N):
    n = N
    M = magsteps.main(N=n, ntimesteps=10**3, T=2.5, metropolis=True, 
                                                          wolff=False).T[1]
    out = tau_e(acf(M))
    return out


N_arr = np.array([4, 8])

#metropolis_arr = np.array([metropolis(N=n) for n in N_arr])

#wolff_arr = np.array([wolff(N=n) for n in N_arr])

#metropolis = np.vstack((N_arr, metropolis_arr)).T

#wolff = np.vstack((N_arr, wolff_arr)).T

#np.savetxt("metropolis", metropolis, header="N, tau_e")

#np.savetxt("wolff", wolff, header="N, tau_e")

wol = np.loadtxt('wolff').T

xdata = np.log(wol[0])

poptw, pcovw = optimize.curve_fit(line, xdata, wol[1])

plt.figure()
plt.plot(xdata, wol[1], '.', label='wolff')
plt.plot(np.linspace(xdata.min(), xdata.max()), line(np.linspace(xdata.min(), xdata.max()), *poptw), 'b--', label='z_w=%5.3f ' % poptw[0])
plt.legend()
