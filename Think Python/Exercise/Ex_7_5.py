# Ramanujan formula for pi

from math import sqrt, factorial 

def estimate_pi():
    '''
    Use Ramanujan formula to estimate pi
    '''
    x = 1
    k = 0
    s = 0
    while x > 10**(-15):
        x = factorial(4*k)*(1103+26390*k) / (factorial(k)**4 * 396**(4*k))
        s = s + x
        k = k + 1
    return 9801/(2*sqrt(2)*s)


# Test code
print(estimate_pi())

