from math import pi


class Circle(object):
    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = self._get_diameter()
        self.area = self._get_area()

    def __str__(self):
        return 'Circle({})'.format(str(self.radius))

    def __repr__(self):
        return 'Circle({})'.format(str(self.radius))

    def _get_diameter(self):
        return self.radius*2

    def _get_area(self):
        return (self.radius ** 2) * pi
