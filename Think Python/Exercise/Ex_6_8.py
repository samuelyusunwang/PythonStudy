# GCD: greatest common divisor ot a and break

def gcd(a, b):
    '''
    Use recursion (Euclid algo) to find the GCD of a and b
    '''
    if a==0 and b!=0:
        return b
    elif a!=0 and b==0:
        return a
    else:
        return gcd(b, a%b)
    
    

# Test code
print(gcd(28, 23))