import matplotlib.pyplot as plt
from math import atan, degrees
import mplcyberpunk
from tabulate import tabulate


def deg(D2, L):
  D1 = 0.004 # Laser Beam Diameter at the Output
  # Calculating of Divergence Angle of Beam
  return [round(degrees(atan((d2 - D1) / (2 * l))), 3) for d2, l in zip(D2, L)]


# Data
# Laser Beam Diameter on a Display
D2 = [i / 1000 for i in [4, 6, 8, 10, 12, 15, 16, 17]]
# Distance from the Laser
distance = list(range(1, 9))


# Calculating of Divergence Angle
alpha = deg(D2, distance)
average = round(sum(alpha) / len(alpha), 3)


# Making Data Table
head = ['Lenth, m', 'Diameter, m', 'Divergence angle, degrees']
data = zip(distance, D2, alpha)


# Plotting a graphics
plt.style.use("cyberpunk")
plt.title('Divergence angle', fontsize=15)
plt.xlabel('Distance from the Laser, m', fontsize=15)
plt.ylabel('Laser Beam Diameter on a Display, m', fontsize=15)
plt.plot(distance, D2, marker='o', color='m')
plt.legend()
mplcyberpunk.add_glow_effects()


# Printing
print(tabulate(data, headers=head, tablefmt='psql'))
print(f'\nAverage of Divergence Angle: {average}')

input('ENTER to plot')

plt.show()
