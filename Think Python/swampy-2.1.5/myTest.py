from TurtleWorld import *
from math import pi

def square(t, length=100):
	'''
	Draw a square using Turtle t. 
	'''
	for i in range(4):
		fd(t, length)
		lt(t)
		
def polygon(t, length=8, n=4):
	'''
	Draw a polygon
	'''
	for i in range(n):
		fd(t, length)
		lt(t, 360/n)

def circle(t, r):
	'''
	Draw a circle
	'''
	n = 20
	polygon(t, 2*pi*r/n, n)
	
def arc(t, r, angle):
	'''
	Draw an arc
	'''
	n = 20
	m = int(angle*n/360)
	for i in range(m):
		fd(t, 2*pi*r/n) 
		lt(t, 360/n)

############################

# Test
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

# square(bob)
# polygon(bob, 8, 8)
# circle(bob, 100)
arc(bob, 100, 90)

wait_for_user()

