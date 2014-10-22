# Test the square root algorithm (Newton)

from Ex_7_2 import square_root
from math import sqrt

def test_square_root():
    i = 1
    while i <= 9:
        print( i, square_root(i), sqrt(i), abs(square_root(i)-sqrt(i)) )
        i = i + 1



# Test code
test_square_root()