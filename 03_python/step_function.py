# step_function.py
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2017/01/19/03_Introduction_to_Python_2/#activity-plotting-the-step-function

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

# list of x values for plotting
# from -4 to 4 in steps of 0.5
xmin, xmax, h = -4, 4, 0.5

# list comprehension (more compact than a for-loop); note that
# +1 is needed in the range() argument to include the last value, +4.
X = [xmin + i*h for i in range(int((xmax - xmin)/h) + 1)]

# evaluate  y = Theta(x)
Y = [heaviside(x) for x in X]

# output as a table
for x, y in zip(X, Y):
    print(x, y)

# plot and save figure
plt.plot(X, Y, '-o', color="red", linewidth=2)
plt.show()
plt.savefig("step_function.png")
