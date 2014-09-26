# Ex 6.1 Compare two values
from math import sqrt

def compare(x, y):
    '''
    compare x and y
    '''
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1
    
# Ex 6.2 calculate hypotenuse
def hypotenuse(a, b):
    '''
    calculate the hypotenuse of a right triangle
    '''
    c = sqrt(a**2 + b**2)
    return c

# Ex 6.3 Check if y is between x and z
def is_between(x, y, z):
    '''
    Check if y is between x and z
    '''
    return x<=y and y<=z
    

# Test 
print(compare(1, 1.2))
print(compare(2, 2))
print(compare(0.3, 0.1))

print(hypotenuse(3,4))

print(is_between(3.1,3,4))