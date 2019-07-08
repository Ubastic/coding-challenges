from math import pi


class Sphere(object):
    def __init__(self, radius, mass):
        self._radius = radius
        self._mass = mass

    def get_radius(self):
        return self._radius

    def get_mass(self):
        return self._mass

    def get_volume(self):
        return round(4.0 / 3.0 * pi * self._radius ** 3, 5)

    def get_surface_area(self):
        return round(4.0 * pi * self._radius ** 2, 5)

    def get_density(self):
        return round(self._mass / (4.0 / 3.0 * pi * self._radius ** 3), 5)
