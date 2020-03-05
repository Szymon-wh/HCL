import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:

    """A class representing a circle"""

    def __init__(self, x=1, y=1, radius=1):
        if radius < 0:
            raise ValueError("negative radius")
        self.radius = radius
        self.pt = Point(x, y)



    def __repr__(self):
        return '{} \n{} {} {}\n{}'.format(self.area(), self.radius, self.move(self.pt.x, self.pt.y), self.pt.y,
                                          self.cover(10))

          # "Circle(x, y, radius)"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.floor(math.pi * (self.radius ** 2))

    def move(self, x, y):
        return self.pt.x + x, self.pt.y + y


        # shift by (x, y)

    def cover(self, other):
        l = math.sqrt((self.pt.x - other.pt)**2 + (self.pt.y - other.pt)**2) + self.radius + other.radius
        # circle covering both
        return l

kolo = Circle(11,22,10,)

print(kolo)

