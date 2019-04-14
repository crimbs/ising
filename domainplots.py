import numpy as np
import matplotlib.pyplot as plt


# Load data from files
N4 = np.loadtxt('N4').T
N8 = np.loadtxt('N8').T
N16 = np.loadtxt('N16').T

# X-axis for plots
T_c = 2 / np.log(1 + np.sqrt(2))
T = np.linspace(1, 5, num=50)
t = (T - T_c) / T_c


# Typical domain size per spin
plt.figure()
plt.plot(t, N16[5], '.', label='$N=16$')
plt.plot(t, N8[5], '.', label='$N=8$')
plt.plot(t, N4[5], '.', label='$N=4$')
plt.xlabel('$T/T_c$')
#plt.ylabel('Typical Domain Size')
plt.title('Typical domain size per spin')
plt.legend()
