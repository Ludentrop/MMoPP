import matplotlib.pyplot as plt
import numpy as np
import mplcyberpunk


A = 75 * 10**4
L = 59 / 100 #m
d = 7.5 #mm
Ip = .023 #A
Ua = 7.6 * 1000 #V
Sk = 3.3/10000 #cm^2
fi = 4.52 #V
k = 1.38 * 10**-23
E0 = 8.85 * 10**-12
e = 1.6 * 10**-19
l = L * .85

E = round(Ua / l, 4)
je = Ip/Sk

x = []
j = []

for T in np.linspace(2070, 2150, 50):
    e1 = -(e*fi/k) / T
    e2 = ((e**1.5)/((4*np.pi*E0)**.5*k)) / T

    res = A * T ** 2 * np.e ** e1 * np.e ** e2

    x.append(T)
    j.append(res)


plt.style.use('cyberpunk')

plt.title('The function of electron emission from the cathode temperature',
          fontsize=15, fontstyle='italic')
plt.xlabel('Temperature, K', fontsize=12)
plt.ylabel('Electron emitting, mA', fontsize=12)

plt.plot(x, j, label='The main function')
plt.scatter(2128.7755102040815, 69.18794578046423, color='red',
            linewidths=13, label='The point of the function')
plt.scatter(2127, je, color='m', linewidths=13, label='Je/Ip')

plt.legend()
plt.show()














# 1 особ молек лаз 2 разновид 3 харак 4 эн диаг 5 принцип дейст 6 преим недост 7 примен 8 конструкция
