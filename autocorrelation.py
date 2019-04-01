# author: Christian Hines
# date: March 2019
# autocorrelation.py
import numpy as np
from ising_class import Ising
import time
import matplotlib.pyplot as plt
start = time. time()

def ACF(x,max_lag):
    x = np.array(x)
    N = len(x)
    
    Mbar = np.mean(x)
    A0 = sum(((x - Mbar)**2)/(N - 1))
    
    out = [1]
    for lag in range(1,max_lag):
        out += [sum((x[lag:] - Mbar)*(x[:(N-lag)] - Mbar)/((N-lag-1)*A0))]
    
    plt.bar(range(0,max_lag),out)
    
x = np.random.randn(1)

i = 1
while i <100:
    xnew = list(x[-1]+ np.random.randn(1))
    x = np.array(list(x)+xnew)
    i += 1
  
plt.figure()
plt.plot(x)   
plt.figure()
ACF(x,50)

end = time.time()
print(end - start)




    


