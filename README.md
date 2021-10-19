## The Ising Model of a Ferromagnet

### Background

In his 1924 PhD thesis \cite{ising}, Ising erroneously predicted - based on his investigation into the one-dimensional model - that there were no phase transitions for any lattice dimension $d$ with temperature $T>0$. However, it has since been shown that abrupt phase transitions occur for lattices with dimensions $d \geq 2$. In 1944, Lars Onsager published his proof for the two-dimensional Ising model, containing his analytical result for the critical temperature for an infinite lattice
$$\frac{k_{B} T_{c}}{J} = \frac{2}{\ln(1+\sqrt{2})} = 2.269185\ldots$$

### Summary

The investigation involved writing a Python program to implement the Metropolis algorithm for the two-dimensional Ising model. Various properties of the model were obtained using computational methods and compared with the theoretical expectations. In particular; autocorrelation, statistical error, hysteresis, response functions, finite-size scaling, domain size, and finally comparing the Metropolis algorithm to Wolff's cluster-flipping algorithm.

### Definition of the Ising Model

Consider $N \times N$ sites on a two-dimensional square lattice where each site is occupied by a spin $s_i = \pm1$ where the positive and negative correspond to spin-up and spin-down respectively. The energy of the system is then given by
$$E = -J \sum_{<i,j>} s_{i} s_{j} - \mu H \sum_{i=1}^{N^2} s_{i}$$
Here $<i,j>$ runs over the nearest-neighbours, $J$ is the exchange energy, $\mu$ is the magnetic moment and $H$ is the external field. The regime where $J>0$ corresponds to ferromagnetism, since the spins favour alignment. There is therefore a `competition' between the exchange energy $J$ trying to align the spins and the thermal energy $k_{B}T$ trying to randomise the spins. To simplify the problem, we set $J=k_{B}=1$ (Thus $T$ is measured in units of $J/k_{B}$). In order to avoid edge effects, the two-dimensional square lattice is mapped onto a torus $\mathbf{T}^{2} = S^{1} \times S^{1}$ by imposing suitable periodic boundary conditions.