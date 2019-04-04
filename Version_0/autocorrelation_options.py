# author: Ollie Hines
# date: March 2019
# autocorrelation.py
import numpy as np
import matplotlib.pyplot as plt
import ising
import time

#----------hybrid--------------#


def acf(M, nlags=40):
    """
    Autocorrelation for 1D array
    """
    Mdash = M - np.mean(M)
    N = len(M)
    d = N * np.ones(2 * N - 1)
    acov = (np.correlate(Mdash, Mdash, 'full') / d)[N - 1:]
    acf = acov[:nlags + 1] / acov[0]
    return acf

#---------- stats lib--------------#

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


def acf0(x, nlags=40, unbiased=False):
    """
    Autocorrelation function for 1D
    """
    if unbiased:
        avf = acovf(x, unbiased=False)
    else:
        avf = acovf(x, unbiased=True)

    acf = avf[:nlags + 1] / avf[0]
    return acf


#----------OLLIES VERSIOn________________#


def ACF(M, nlags=41):
    """
    Returns correlation
    """
    M = np.array(M)
    N = len(M)
    M_av = np.mean(M)
    Mdash = M - M_av
    A0 = np.sum(((Mdash)**2) / (N - 1))
    out = [1]
    for lag in range(1, nlags):
        out += [sum((M[lag:] - M_av) * (M[:(N - lag)] - M_av) /
                    ((N - lag - 1) * A0))]
    return out
