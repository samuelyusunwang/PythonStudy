# Examples of object

from math import sqrt
from copy import deepcopy

# Point object
class Point(object):
    """ represents a point in 2-D space """
    
class Rectangle(object):
    '''
     represents a rectangle.
     attributes: width, height, corner.
    '''

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

    
# Ex 15.1
def distance(p1, p2):
    return sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

# Ex 15.2
def move_rectangle1(box, dx, dy):
    box.corner.x += dx
    box.corner.y += dy
    
# Ex 15.3
def move_rectangle2(box, dx, dy):
    box_new = deepcopy(box)
    move_rectangle1(box_new, dx, dy)
    return box_new

# Test code
p1 = Point(); p1.x = 3.0; p1.y = 0.0
p2 = Point(); p2.x = 0.0; p2.y = 4.0

print(distance(p1,p2))

box1 = Rectangle()
box1.width = 100.0
box1.height = 200.0
box1.corner = Point()
box1.corner.x = 0.0
box1.corner.y = 0.0
move_rectangle1(box1, 5, 6)
print_point(box1.corner)

box2 = move_rectangle2(box1, -5, -6)
move_rectangle1(box1, -5, -6)
print(box2 is box1)
