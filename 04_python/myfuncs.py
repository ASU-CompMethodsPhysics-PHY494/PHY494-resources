# function module

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
    """Convert temperature theta in F to K"""
    return 5/9*(theta - 32) + 273.15

def kelvin2celsius(T):
    """Convert temperature T in K to degree Celsius"""
    return T - 273.15

