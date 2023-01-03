import matplotlib.pyplot as plt
import mplcyberpunk
import numpy as np


# Creating Data
x = np.arange(0, 2*np.pi, 0.1)
y1 = np.cos(x/2)**2
y2 = np.sin(x/2)**2


# Plotting
plt.style.use('cyberpunk')
plt.title('Stern-Gerlach experiment', fontsize=15)
plt.xlabel('alpha', fontsize=15)
plt.ylabel('Probability', fontsize=15)
plt.plot(x, y1, '-r',)
plt.plot(x, y2, '-b',)
plt.legend(['P(+)=cos^2(alpha/2)', 'P(-)=sin^2(alpha/2)'])
mplcyberpunk.add_glow_effects()

plt.show()
