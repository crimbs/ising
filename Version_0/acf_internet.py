import numpy as np
import scrapheapchallenge

M = scrapheapchallenge.main(N=8, T=5, num_steps=10**3)[0]
N = np.size(M)
k = 5
M_av = np.average(M)

def autocovariance(Xi, N, k, Xs):
    autoCov = 0
    for i in np.arange(0, N-k):
        autoCov += ((Xi[i+k])-Xs)*(Xi[i]-Xs)
    return (1/(N-1))*autoCov

def autocorrelation():
    return autocovariance(M, N, k, M_av) / autocovariance(M, N, 0, M_av)

print("Autocovariance:", autocovariance(M, N, k, M_av))
print("Autocorrelation:", autocorrelation())