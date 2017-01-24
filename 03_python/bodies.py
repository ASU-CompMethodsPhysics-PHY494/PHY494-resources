# basic object oriented programming
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2017/01/19/03_Introduction_to_Python_2/#objects

import math

class Sphere:
   """A simple sphere."""

   def __init__(self, pos, radius=1):
       self.pos = tuple(pos)
       self.radius = float(radius)

   def volume(self):
       return 4/3 * math.pi * self.radius**3

   def translate(self, t):
       self.pos = tuple(xi + ti for xi, ti in zip(self.pos, t))

class Planet(Sphere):
   def __init__(self, name, pos, mass, radius):
       self.name = str(name)
       self.pos = tuple(pos)
       self.mass = float(mass)
       self.radius = float(radius)

   def density(self):
       """Compute density of the planet"""
       return self.mass / self.volume()


if __name__ == "__main__":
    # This part is only executed if the file is run through the Python
    # interpreter. If it is imported as a module then the whole if
    # block will be skipped. This the canonical way to write scripts
    # in Python: put the script in this block.

    # http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2017/01/19/03_Introduction_to_Python_2/#creating-objects-classes

    print("Instantiate ball = Sphere((0, 0, 10), radius=2)")
    ball = Sphere((0, 0, 10), radius=2)
    print("type(ball)", type(ball))


    # http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2017/01/19/03_Introduction_to_Python_2/#attributes-and-methods

    print("ball.pos", ball.pos)
    print("ball.radius", ball.radius)

    print("Set attribute     ball.pos = (-5, 0, 0)")
    ball.pos = (-5, 0, 0)
    print("ball.pos", ball.pos)

    print("ball.volume()", ball.volume())

    ball.translate((5, 0, 0))
    print("ball.pos", ball.pos, "after ball.translate((5, 0, 0))")

    # http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2017/01/19/03_Introduction_to_Python_2/#independence-of-instances
    print("Instantiate ball and ballon at (0, 0, 10)")
    ball = Sphere((0, 0, 10), radius=2)
    balloon = Sphere((0, 0, 10), radius=6)

    ball.pos = (-1, -1, 0)
    print("ball.pos", ball.pos, "after ball.pos = (-1, -1, 0)")
    print("balloon.pos", balloon.pos)


    # http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2017/01/19/03_Introduction_to_Python_2/#inheritance
    # quantities from http://www.wolframalpha.com
    # lengths in m and mass in kg
    print('Instantiate earth = Planet("Earth", (1.4959802296e11 , 0, 0), 5.9721986e24, 6371e3)')
    earth = Planet("Earth", (1.4959802296e11 , 0, 0), 5.9721986e24, 6371e3)
    print("earth.density()", earth.density())
