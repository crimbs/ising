import matplotlib.pyplot as plt
import ising
import stats

M = ising.main(N=8, T=5, nsteps=10**3, mag=True, everystep=False)
y = stats.acf(M, nlags=10)

# ACF plot
plt.figure()
plt.bar(range(len(y)), y)
plt.xlabel('lag')
plt.ylabel('ACF')
plt.xlim(0, len(y))