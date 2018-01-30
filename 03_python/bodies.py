# Basic lesson on object oriented programming: bodies.py
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/page2/#creating-objects-classes-advanced-topic

"""How to use the objects in this module:

>>> from bodies import Sphere
>>> ball = Sphere((0, 0, 10), radius=2)
>>> ball.pos = (-5, 0, 0)

Use a method to calculate the volume:

>>> print(ball.volume())


Move the position:

>>> ball.translate((5, 0, 0))
>>> print(ball.pos)


Make a second instance:

>>> balloon = Sphere((0, 0, 10), radius=6)
>>> ball.pos = (-1, -1, 0)
>>> print(ball.pos, balloon.pos)


"""


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
    """A planet"""
    def __init__(self, name, pos, mass, radius):
        self.name = str(name)
        self.pos = tuple(pos)
        self.mass = float(mass)
        self.radius = float(radius)

    def density(self):
        """Compute density of the planet"""
        return self.mass / self.volume()


if __name__ == "__main__":

    # quantities from http://www.wolframalpha.com
    # lengths in m and mass in kg

    earth = Planet("Earth", (1.4959802296e11 , 0, 0), 5.9721986e24, 6371e3)
    print("Earth density", earth.density())
