import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def least_squares(x_arr, y_arr):
    size = x_arr.shape[0]

    b=(np.sum(y_arr) * np.sum(x_arr * x_arr) - np.sum(x_arr) * np.sum(x_arr * y_arr)) / (size * np.sum(x_arr * x_arr) - np.sum(x_arr) * np.sum(x_arr))

    a = (np.sum(y_arr) - size * b)/np.sum(x_arr)

    return a, b

data = np.loadtxt("data.txt")

settings = np.loadtxt("settings.txt", skiprows=1)

n = settings[0]
dv = settings[1]

v = data[:]*dv
t = np.arange(0, len(v))/settings[0]

n_markers = 10
s=round(t[len(v)-1], 2)

fig = plt.figure(figsize=(7.5, 7.5))

ax = fig.add_subplot()

plt.title(label="Зарядка конденсатора", fontsize=12, fontweight='bold', pad=10)

ax.plot(t, v, color = "b", marker='.', ms=15, markevery=n_markers)

ax.set(xlim=(0, 11), ylim=(0, 2.8))

ax.set_xlabel('t, с', fontweight='bold')
ax.set_ylabel('U, В', fontweight='bold')
plt.legend(['зависимость U(t)', 'некоторые точки'])
ax.text(7, 1.6, 'время зарядки = 10.32 c', color='black', fontsize=10)


ax.xaxis.set_major_locator(MultipleLocator(base = 1))
ax.yaxis.set_major_locator(MultipleLocator(base = 0.5))

ax.xaxis.set_minor_locator(MultipleLocator(base = 0.5))
ax.yaxis.set_minor_locator(MultipleLocator(base = 0.1))

ax.grid(which='major', linewidth=1)
ax.grid(which='minor', linewidth=0.3)
plt.show()