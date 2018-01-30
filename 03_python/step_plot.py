# plotting the Heaviside function
# https://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/#activity-plotting-the-step-function

import matplotlib.pyplot as plt

def heaviside(x):
   """Heaviside step function"""

   theta = None
   if x < 0:
      theta = 0.
   elif x == 0:
      theta = 0.5
   else:
      theta = 1.

   return theta


# generate x values

xmin, xmax, h = -4, 4, 0.5
nx = int((xmax - xmin)/h + 1)

xvalues = []
for i in range(nx):
    xvalues.append(xmin + i*h)


# evaluate theta(x)

thetas = []
for x in xvalues:
    thetas.append(heaviside(x))

# print table
for x, y in zip(xvalues, thetas):
    print(x, y)

# plot (optional)
plt.plot(xvalues, thetas, '-o', color="red", linewidth=2)
plt.show()

# write to a file
plt.savefig("heaviside.png")
