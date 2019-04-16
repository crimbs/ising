import numpy as np
import matplotlib.pyplot as plt

H = np.linspace(-2, 2, num=50)

T1 = np.loadtxt('data/T1').T
T2 = np.loadtxt('data/T2').T
T3 = np.loadtxt('data/T3').T

plt.plot(H, T1[1])
plt.plot(H, np.flip(T1[2]))
plt.plot(H, T2[1])
plt.plot(H, np.flip(T2[2]))
plt.plot(H, T3[1])
plt.plot(H, np.flip(T3[2]))
plt.xlabel('$H$')
plt.ylabel('$M$')

