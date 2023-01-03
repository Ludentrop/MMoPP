import matplotlib.pyplot as plt
from math import atan, degrees
import mplcyberpunk
from tabulate import tabulate
from textwrap import wrap


# Data
Ip = [4 * i for i in range(3, 11)]
Pp = [2, 13.5, 27, 33, 38, 42, 47, 49]
Is = 9
m = len(Ip)


# Calculating
# Sigma
sigma1 = sum(Ip)
sigma2 = sum(i * i for i in Ip)
sigma3 = sum(Pp)
sigma4 = sum(i * p for i, p in zip(Ip, Pp))

# Coefficients
denominator = (m * sigma2 - sigma1 ** 2)
calculated_empirical_coefficient =  round((m * sigma4 - sigma3 * sigma1) / denominator, 3)
calculated_coefficient = round((sigma3 * sigma2 - sigma4 * sigma1) / denominator, 3)

# Laser Radiation Power
def laser_radiation_power(Ip):
    return calculated_empirical_coefficient * Ip + calculated_coefficient

P = [round(laser_radiation_power(i), 3) for i in Ip]


# Making Data Table
head = ['Ip, mA', 'Pp, mW']
data = zip(Ip, Pp)


# Plotting
plt.style.use("cyberpunk")
plt.title("\n".join(wrap("Empirical and theoretical laws describing the effect of the discharge current on the generated laser power", 60)))
plt.xlabel('Ip, mA', fontsize=15)
plt.ylabel('Pp, mW', fontsize=15)
plt.plot(Ip, Pp, label='Theoretical', marker='o')
plt.plot(Ip, P, label='Empirical', marker='o')
plt.legend()
mplcyberpunk.add_glow_effects()


# Printing
print(tabulate(data, headers=head, tablefmt='psql'))

print(f'\nSigma1: {sigma1}\n',
      f'Sigma2: {sigma2}\n',
      f'Sigma3: {sigma3}\n',
      f'Sigma4: {sigma4}\n', sep='')

print(f'Calculated Empirical Coefficient: {calculated_empirical_coefficient}\n',
      f'Calculated Coefficient: {calculated_coefficient}', sep='')

input('ENTER to plot')

plt.show()
