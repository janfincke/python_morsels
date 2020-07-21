from math import pi


class Circle(object):
    def __init__(self, radius=1):
        self._radius = radius
        self._diameter = 0
        self._area = 0

    def __str__(self):
        return 'Circle({})'.format(str(self._radius))

    def __repr__(self):
        return 'Circle({})'.format(str(self._radius))

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        self._diameter = self._radius * 2
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError("Diameter cannot be negative")
        self._diameter = value * 2
        self._radius = value / 2

    @property
    def area(self):
        self._area = (self._radius ** 2) * pi
        return self._area

    @area.setter
    def area(self, value):
        raise AttributeError("can't set attribute")
