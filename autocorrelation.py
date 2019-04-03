# author: Ollie Hines
# date: March 2019
# autocorrelation.py
import numpy as np
import matplotlib.pyplot as plt
import ising

M = ising.main(N=8, T=5, nsteps=10**3)[0]


def acovf(x, unbiased=False):
    """
    Autocovariance for 1D
    """
    x = np.array(x)
    xdash = x - np.mean(x)
    n = len(x)
    if unbiased:
        xi = np.arange(1, n + 1)
        d = np.hstack((xi, xi[:-1][::-1]))
    else:
        d = n * np.ones(2 * n - 1)
    acov = (np.correlate(xdash, xdash, 'full') / d)[n - 1:]
    return acov


def acf(x, nlags=40, unbiased=False):
    """
    Autocorrelation function for 1D
    """
    if unbiased:
        avf = acovf(x, unbiased=False)
    else:
        avf = acovf(x, unbiased=True)

    acf = avf[:nlags + 1] / avf[0]
    return acf


isthis = acf(M, unbiased=True)

#----------OLLIES VERSIOn________________#


def ACF(x, max_lag):
    '''
    Returns autocovariance
    '''
    x = np.array(x)
    N = len(x)
    M_av = np.mean(x)
    A0 = sum(((x - M_av)**2) / (N - 1))
    out = [1]
    for lag in range(1, max_lag):
        out += [sum((x[lag:] - M_av) * (x[:(N - lag)] - M_av) /
                    ((N - lag - 1) * A0))]
    return out


# Plot variables
max_lag = 40

# ACF plot
plt.figure()
plt.bar(range(0, max_lag), ACF(M, max_lag))
plt.xlabel('lag')
plt.ylabel('ACF(cov)')


plt.figure()
plt.bar(range(len(isthis)), isthis)
plt.xlabel('lag')
plt.ylabel('ACF(cov)')
