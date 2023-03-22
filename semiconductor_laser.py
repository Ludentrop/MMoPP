import matplotlib.pyplot as plt
import mplcyberpunk
from tabulate import tabulate


U = [1.6, 1.9, 2.2, 2.5, 2.8, 3.1, 3.4, 3.7]
Upn = [1.49, 1.63, 1.72, 1.84, 1.88, 1.91, 1.95, 2.02]
I = [0, 6, 12.5, 19.5, 26.5, 32, 40, 48]
Pcon = [u*i for u, i in zip(U, I)]
Pgen = [x*.6 for x in Pcon]

head = ['U, B', 'Upn, B', 'I, mA', 'Pпот, W', 'Pген, W']
data = zip(U, Upn, I, Pcon, Pgen)


# Plotting a graphics
plt.style.use("cyberpunk")
plt.title('ВАХ GaAs-лазера', fontsize=15)
plt.xlabel('U, V', fontsize=15)
plt.ylabel('I, mA', fontsize=15)
plt.plot(Upn, I, marker='o', color='m')
plt.legend()
mplcyberpunk.add_glow_effects()


# Printing
print(tabulate(data, headers=head, tablefmt='psql'))

plt.show()
