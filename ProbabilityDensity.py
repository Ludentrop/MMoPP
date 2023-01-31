import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk


def psi_squared(x, A=1, alpha=1, n=0):
    return A**2 * np.sin(np.pi/alpha * (n+1) * x)**2


x = np.linspace(0, 1, 100)
psi0 = [psi_squared(i, n=0) for i in x]
psi1 = [psi_squared(i, n=1) for i in x]
psi2 = [psi_squared(i, n=2) for i in x]

labels = ['n=0', 'n=1', 'n=2']
colors = ['m', 'b', 'r']
psis = [psi0, psi1, psi2]

plt.style.use('cyberpunk')
fig, axs = plt.subplots(3, figsize=(10, 6))

for i, ax in enumerate(axs):
  axs[i].plot(x, psis[i], color=colors[i], label=labels[i])
  axs[i].legend(loc='upper left')
  axs[i].set_ylabel('Probability', fontsize=12, fontstyle='italic')

fig.suptitle('$\Psi$ Function Probability Density', fontsize=16, fontstyle='italic')
fig.supxlabel('Barrier Width', fontsize=12, fontstyle='italic')
plt.show()
