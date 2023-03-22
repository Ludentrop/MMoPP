import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk


def psi(x, n, A=1, alpha=1):
    return A * np.sin(n*x*np.pi/alpha)


def psi_squared(x, n, A=1, alpha=1):
    return A**2 * np.sin(np.pi/alpha*n*x)**2


x = np.linspace(0, 1, 100)
psi1 = [psi(i, 1) for i in x]
psi2 = [psi(i, 2) for i in x]
psi3 = [psi(i, 3) for i in x]

psi_squared1 = [psi_squared(i, 1) for i in x]
psi_squared2 = [psi_squared(i, 2) for i in x]
psi_squared3 = [psi_squared(i, 3) for i in x]

labels = [['n=3', 'n=3'], ['n=2', 'n=2'], ['n=1', 'n=1']]
colors = [['m', 'm'], ['b', 'b'], ['r', 'r']]
psis = [[psi3, psi_squared3], [psi2, psi_squared2], [psi1, psi_squared1]]

plt.style.use('cyberpunk')
fig, axs = plt.subplots(3, 2, sharex=True, sharey=False, figsize=(10, 6))

for i in range(3):
    for j in range(2):
        axs[i][j].plot(x, psis[i][j], color=colors[i][j], label=labels[i][j])
        axs[i][j].legend(loc='upper right')


fig.suptitle('\t\tEigenfunction\t\t\t\t\t $\Psi$ Function Probability Density', fontsize=16, fontstyle='italic', ha='center')
fig.supxlabel('Barrier Width', fontsize=15, fontstyle='italic')
fig.supylabel('Wave function and Probability', fontsize=15, fontstyle='italic')
plt.show()
