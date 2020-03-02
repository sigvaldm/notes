import matplotlib as mp
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6*np.pi, 100)
x = np.cos(t)

# plt.plot(t,x)
# plt.xlabel('t [s]')
# plt.ylabel('x [m]')
# # plt.title('Position of a harmonic oscillator')
# plt.savefig('poorfig.png')
# plt.show()

fig, ax = plt.subplots(constrained_layout=True)
ax.plot(t,x)
ax.set_xlabel('$t$ [s]')
ax.set_ylabel('$x$ [m]')
plt.savefig('poorfig.png')
plt.show()

mp.rc('text', usetex=True)
mp.rc('font', family='serif', size=10, serif='Computer Modern Roman')
# mp.rc('font.serif', 'Computer Modern Roman')
mp.rc('axes', titlesize=10)
mp.rc('axes', labelsize=10)
mp.rc('xtick', labelsize=10)
mp.rc('ytick', labelsize=10)
mp.rc('legend', fontsize=10)
mp.rc('figure', titlesize=10)

figsize = np.array([75, 75/1.618])
dpi = 300
fig, ax = plt.subplots(figsize=figsize/25.4, constrained_layout=True, dpi=157.35)
ax.plot(t,x)
ax.set_xlabel('$t$ [s]')
ax.set_ylabel('$x$ [m]')
# ax.set_title('Position of a harmonic oscillator')
plt.savefig('goodfig.png', dpi=dpi)
plt.show()

