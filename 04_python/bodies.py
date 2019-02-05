# 04 Python: Objects
# https://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2019/01/31/04_Introduction_to_Python_4/#objects


import math

class Sphere:
    """A simple sphere."""

    def __init__(self, pos, radius=1):
        """
        Parameters
        ----------
        pos : list or tuple
              position of the center (x, y, z)
        radius : float (optional)
              radius of the sphere, default is 1

        """
        self.pos = tuple(pos)
        self.radius = float(radius)

    def volume(self):
        """Return the volume of the sphere"""
        return 4/3 * math.pi * self.radius**3

    def translate(self, t):
        """Move the sphere by vector t.

        The position of the shere (attribute Sphere.pos)
        is changed by adding t.

        Parameters
        ----------
        t : list or sequence
            translation vector

        """
        self.pos = tuple(xi + ti for xi, ti in zip(self.pos, t))



class Planet(Sphere):
    """A spherical planet.

    Attributes
    ----------
    name : string
           name
    pos :  tuple
           coordinates
    mass : float
           mass in kg
    radius : float
           radius in km
    """

    def __init__(self, name, pos, mass, radius):
        """
        Parameters
        ----------
        name : string
               name
        pos :  tuple or list
               coordinates (x, y, z)
        mass : float
               mass in kg
        radius : float
               radius in km
        """
        self.name = str(name)
        self.pos = tuple(pos)
        self.mass = float(mass)
        self.radius = float(radius)

    def density(self):
        """Return the density of the planet"""
        return self.mass / self.volume()

