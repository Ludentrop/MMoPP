import matplotlib.pyplot as plt
import mplcyberpunk
from tabulate import tabulate



x = [0, 750, 1050, 1350, 1800, 1950, 2150, 2600, 2800]
y = [380, 440, 480, 510, 560, 600, 650, 750, 850]


A = [0, 500, 1000, 1500, 1700, 1800, 2250, 2400, 2800, 3150, 3250, 3400, 3500, 3600]
U = [0.005, 0.008, 0.007, 0.075, 0.11, 0.135, 0.2, 0.23, 0.27, 0.3, 0.305, 0.295, 0.265, 0.1]


plt.style.use('cyberpunk')
plt.plot(A, U)
plt.show()
