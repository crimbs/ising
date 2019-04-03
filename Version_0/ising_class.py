# author: Christian Hines
# date: March 2019
# ising_class.py
import numpy as np
import time
start = time.time()

class Ising:
    
    def __init__(self, N=8, T=1, num_steps=10**3):
        self.N = N
        self.T = T
        self.num_steps = num_steps
    
    def lattice(self):
        return np.int8(np.random.choice([1, -1], size=(self.N, self.N)))
        
    def magnetisation(self):
        
        time_step = self.N**2
        
        total_steps = self.num_steps*time_step
        
        lattice = self.lattice()
        
        lattice_picker = np.random.randint(self.N, size=(total_steps, 2))

        boltzmann_picker = np.random.rand(total_steps)
        
        for step in range(total_steps):
            
            i = tuple(lattice_picker[step])
            
            dE = lattice[i] * lattice[((i[0] - 1) % self.N), i[1]] + \
                 lattice[((i[0] + 1) % self.N), i[1]] + \
                 lattice[i[0], ((i[1] - 1) % self.N)] + \
                 lattice[i[0], ((i[1] + 1) % self.N)]
                
            if dE < 0 or np.exp(-dE/self.T) > boltzmann_picker[step]:
                lattice[i] = -lattice[i]
                    
        return np.sum(lattice)
    
    @staticmethod
    def dE(self, i, j):
        lattice = self.lattice()
        return lattice[i,j] * lattice[((i - 1) % self.N), j] + \
            lattice[((i + 1) % self.N), j] + \
            lattice[i, ((j - 1) % self.N)] + \
            lattice[i, ((j + 1) % self.N)]
        
def main():
    print( Ising().magnetisation() )

if __name__ == "__main__":
    main()
    
end = time.time()
print(end - start)