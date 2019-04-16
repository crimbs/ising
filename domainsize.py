import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


def getNeighbours(N, i, j):
    """
    Returns a list of neighbour coordinates for the site (i, j)
    """
    neighbours = []
    neighbours.append(tuple([(i + 1) % N, j]))
    neighbours.append(tuple([(i - 1) % N, j]))
    neighbours.append(tuple([i, (j - 1) % N]))
    neighbours.append(tuple([i, (j + 1) % N]))
    return neighbours


def CClabel(lattice):
    """
    Connected-component labeling function with periodic boundary conditions
    """
    N = len(lattice)
    labelled = np.zeros_like(lattice)
    todolist = []
    label = 1
    for i in range(N):
        for j in range(N):
            
            if labelled[i][j] == 0:
                labelled[i][j] = label
                todolist.append((i, j))
                
                while todolist:
                    site = todolist.pop(0)
                    neighbours = getNeighbours(N, *site)
                    
                    for k in [0, 1, 2, 3]:
                        if  lattice[neighbours[k]] == lattice[i][j] and \
                            labelled[neighbours[k]] == 0:   
                            labelled[neighbours[k]] = label
                            todolist.append(neighbours[k])
                label += 1
                
    return labelled


def domain_size(lattice, plot=False):
    """
    Returns the Largest Cluster Size
    """
    N = len(lattice)
    labels = CClabel(lattice)
    area = ndimage.measurements.sum(lattice, labels,
                                    index=np.arange(labels.max() + 1))
    out = np.abs(area[labels])

    if plot:
        plt.figure()
        plt.imshow(out, cmap='gray')
        plt.colorbar()
        plt.axis('off')
        plt.title('Lattice Grouped By Domain Size (N=%i)' % N)

    largest_cluster = out.max()

    return largest_cluster
