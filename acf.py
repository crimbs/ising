import numpy as np
import ising


def acf(M, nlags=10**5):
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
    """
    Returns exponential autocorrelation time tau_e
    """
    exp_factor = 1 / np.exp(1)
    tau_e = len(np.extract(acf >= exp_factor, acf))
    return tau_e
