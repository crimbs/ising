import numpy as np


def acf(M, nlags=10**3):
    """
    Autocorrelation for 1D array
    """
    Mdash = M - np.mean(M)
    N = len(M)
    d = N * np.ones(2 * N - 1)
    acov = (np.correlate(Mdash, Mdash, 'full') / d)[N - 1:]
    acf = acov[:nlags + 1] / acov[0]
    return acf


def tau_e(acf):
    exp_factor = 1 / np.exp(1)
    tau_e = len(np.extract(acf >= exp_factor, acf))
    return tau_e
