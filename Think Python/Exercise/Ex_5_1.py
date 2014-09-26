# Fermat's last theorem

def check_fermat(a, b, c, n):
    '''
    check if a^n + b^n == c^n
    '''
    if a^n + b^n == c^n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work')
        
def check_fermat1(a, b, c, n):
    check_fermat(int(a), int(b), int(c), int(n))


# Test code
# Ex 5.1
check_fermat(3, 4, 5, 3)
check_fermat1(3.3, 3, 5.1, 4.5)