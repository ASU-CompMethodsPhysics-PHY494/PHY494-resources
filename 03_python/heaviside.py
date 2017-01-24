# Heaviside step function http://mathworld.wolfram.com/HeavisideStepFunction.html
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2017/01/19/03_Introduction_to_Python_2/#conditionals
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2017/01/19/03_Introduction_to_Python_2/#functions

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

x = 3
theta = heaviside(x)

print("Theta(" + str(x) + ") = " + str(theta))
