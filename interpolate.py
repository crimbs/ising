import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

N8 = np.loadtxt('N8+').T


T = N8[0]
X = N8[3]
C = N8[4]

f = interpolate.interp1d(T, C)

Tnew = np.linspace(1,5,num=100)
Cnew = f(Tnew) 
plt.plot(T, C, 'o', Tnew, Cnew, '-')