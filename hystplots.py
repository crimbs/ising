import numpy as np
import matplotlib.pyplot as plt
import hysteresis
from scipy import signal


data = hysteresis.main(N=4, T=t, ntimesteps=10**3, nHsteps=50, Hmax=2).T

H = data[0]
up = data[1]
down = np.flip(data[2])

plt.plot(H, up)
plt.plot(H, down)
    
plt.xlabel('$H$')
plt.ylabel('$M$')

from scipy import signal


#from matplotlib2tikz import save as tikz_save
#tikz_save('filename.tex')