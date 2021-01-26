# plot motion with constant acceleration

import matplotlib.pyplot as plt

a = 1.0    # acceleration
v0 = 0.0   # initial velocity

t, h, n = 0.0, 0.1, 20    # init time, step size, number of steps
ta, xa = [], []           # time and position lists

for i in range(n):
    x = v0*t + a*t*t/2.0
    ta.append(t)
    xa.append(x)
    t = t + h

# plot results
plt.figure(figsize=(4, 4))
plt.plot(ta, xa, '-o', color="red", linewidth=2)
plt.xlabel("t (s)")
plt.ylabel("x (m)")

plt.savefig("motion.png")
plt.show()
