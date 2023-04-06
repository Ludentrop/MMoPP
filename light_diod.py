import matplotlib.pyplot as plt
import mplcyberpunk
from tabulate import tabulate


v_red = [1.8, 1.85, 1.89, 2.07]
a_red = [8, 14, 20, 54]

head = ['U, V', 'I, mA']
data = zip(v_red, a_red)

print(tabulate(data, headers=head, tablefmt='psql'))

v_green = [1.76, 1.81, 1.85, 1.93]
a_green = [12, 21, 30, 60]

head = ['U, V', 'I, mA']
data = zip(v_green, a_green)

print(tabulate(data, headers=head, tablefmt='psql'))

input('ENTER to plot')

plt.style.use("cyberpunk")
plt.title('The function of current from voltage')
plt.xlabel('I, mA', fontsize=15)
plt.ylabel('U, V', fontsize=15)
plt.plot(v_red, a_red, color='red', label='For RED light')
plt.plot(v_green, a_green, color='green', label='For GREEN light')
plt.legend()
mplcyberpunk.make_lines_glow()
plt.show()
