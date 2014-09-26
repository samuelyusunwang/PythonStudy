# Ex 6.7

def is_power(a, b):
    '''
    if a is divisible by b;
    and if a/b is a power of b
    '''
    if a%b==0 and (a/b)%b==0:
        return True
    else:
        return False
    

# Test Code
print(is_power(4,2))

print(is_power(5,2))

