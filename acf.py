import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


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


def line(x, m, c):
    """
    Returns equation of line y=mx+c
    """
    return (m * x) + c
