import numpy as np

def wolff(spin,nlist,N,Padd):
    
    stack = np.zeros(N)
    js = np.random.randint(N)
    stack[0] = js
    sp=1
    
    oldspin=spin[js]
    newspin = -1*spin[js]
    spin[js] = newspin
    cluster_size=0
    
    while sp:
        sp = sp - 1
        current = stack[sp]
        for i in range(4):
            if spin[nlist[current][i]] == oldspin: 
                if np.random.rand() < Padd :
                    stack[sp] = nlist[current][i]
                    sp = sp + 1 
                    spin[nlist[current][i]] = newspin
                    cluster_size = cluster_size + 1
                    
    return cluster_size


N=8
stack = np.zeros(N)
js = np.random.randint(N)
stack[0] = js
sp=1
spin = np.ones((N,N))
oldspin=spin[js]
newspin = -1*spin[js]
spin[js] = newspin

cluster_size=0