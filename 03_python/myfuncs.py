# myfuncs.py
#


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


def fahrenheit2kelvin(theta):
    """Convert temperature in Fahrenheit to Kelvin"""

    return 5./9 * (theta - 32) + 273.15

def kelvin2celsius(T):
    """Convert temperature in Kelvin to Celsius"""

    return T - 273.15

