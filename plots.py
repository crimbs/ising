#import numpy as np
import matplotlib.pyplot as plt
import time
import scrapheapchallenge

start = time.time()
test = scrapheapchallenge.main().T
end = time.time()
print(end - start)

start_alt = time.time()
test_alt = scrapheapchallenge.main_alt().T
end_alt = time.time()
print(end_alt - start_alt)

'''
plt.figure()
plt.plot(test[0], label='M')
plt.plot(test[1], label='M_av')
plt.plot(test[2], label='E')
plt.plot(test[3], label='E_av')
plt.legend()
'''