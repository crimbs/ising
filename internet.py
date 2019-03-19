import time
import numpy as np

start = time.time()
# Initialize the system
L = 31
spin = np.ones((L, L))  # 2D square lattice, spin up
T = 300  # 300 K, for temperature
num = 1

# Method 2, using modulus method
np.random.seed(10)
for k in range(num):
    for i in range(L):
        for j in range(L):
            # eflip, the change in the energy of system if we flip the
            # spin[i, j]. eflip depends on the configuration of 4 neighboring
            # spins. For instance, with reference to spin[i, j], we should evaluate
            # eflip based on spin[i+1, j], spin[i-1, j], spin[i, j+1], spin[i, j-1]
            eflip = 2*spin[i, j]*(
                spin[((i - 1) % L), j] +  # -1 in i-dimension
                spin[((i + 1) % L), j] +  # +1 in i-dimension
                spin[i, ((j - 1) % L)] +  # -1 in j-dimension
                spin[i, ((j + 1) % L)]    # +1 in j-dimension
            )
            # Metropolis algorithm
            if eflip == 0.0:
                spin[i, j] = -1.0*spin[i, j]
            else:
                if (np.random.random() == np.exp(-1.0*eflip/T)):
                    spin[i, j] = -1.0*spin[i, j]
 
end = time.time()
print(spin)
print(end - start)