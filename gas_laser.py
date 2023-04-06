import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk


e = 1.6 * 10**-19
k = 1.38 * 10**-23

x = list(range(300, 850, 50))

N100 = lambda T: np.e ** ((2.86 * e - 7.1 * 10 ** -22 * (687 - T)) / (k * T))
N001 = lambda T: (2.81 * T - 842.7) * 10 ** 18

y1 = [N100(t) for t in x]
y2 = [N001(t) for t in x]

# d = abs(y1[0] - y2[0])
#
# for i, j in zip(y1[1:], y2[1:]):
#     if d < abs(i-j):
#         d = abs(i-j)
#     else:
#         print(d, abs(i-j), i, j)


plt.style.use("cyberpunk")
plt.title("Population of the upper and lower energy levels", fontsize=15)
plt.xlabel('Temperature', fontsize=14)
plt.ylabel('1/m^3', fontsize=14)
plt.plot(x, y1, label='N100', marker='s')
plt.plot(x, y2, label='N001', marker='^')
plt.plot([x[5]]*3, [y2[5], y1[5], 0], label='Best zone', marker='o', c='r')

plt.legend()
mplcyberpunk.make_lines_glow()
plt.show()
