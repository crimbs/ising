from scipy import signal
import numpy as np

#import ising

N8 = np.loadtxt('N8+').T

T = N8[0]

X = N8[3]
C = N8[4]

resample_size = 25

X_resample = signal.resample_poly(X, up=resample_size, down=len(T))
C_resample = signal.resample_poly(C, up=resample_size, down=len(T))


Tnew = np.linspace(1, 5, num=resample_size)

import matplotlib.pyplot as plt

plt.figure()
#plt.plot(T, C, 'go-')
plt.plot(Tnew, C_resample, '.-')
plt.legend(['data', 'resampled'], loc='best')

plt.figure()
#plt.plot(T, X, 'go-')
plt.plot(Tnew, X_resample, '.-')
plt.legend(['data', 'resampled'], loc='best')