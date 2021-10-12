import numpy as np

__all__ = ['acf', 'tau_e']

def acf(M, nlags):
    """
    Autocorrelation for 1D array M. nlags is the maximum
    number of lags. Returns 1D autocorrelation array.
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
    as a function of input autocorrelation array.
    """
    exp_factor = 1 / np.exp(1)
    tau_e = len(np.extract(acf >= exp_factor, acf))
    return tau_e
