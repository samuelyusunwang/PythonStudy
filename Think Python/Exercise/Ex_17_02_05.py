# define Point class

class Point(object):
    # initialization
    def __init__(self, x=0, y=0):
        (self.x, self.y) = (x, y)
    # str method
    def __str__(self):
        return '(%f, %f)' % (self.x, self.y)
    # + operator
    def __add__(self, other):
        new_pt = Point()
        if isinstance(other, Point):
            new_pt.x = self.x + other.x
            new_pt.y = self.y + other.y
        else:
            new_pt.x = self.x + other[0]
            new_pt.y = self.y + other[1]
        return new_pt


# Test code
p = Point(3.2, 5.5)
print(p)

print(p + Point(1,4))

print(p + (1,4))