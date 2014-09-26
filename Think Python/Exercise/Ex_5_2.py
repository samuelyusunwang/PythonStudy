# Test triangle formulation
def is_triangle(a, b, c):
    '''
    Determine if a, b, c anc form a triangle
    '''
    if a > b+c:
        print('No')
    elif b > a+c:
        print('No')
    elif c > a+b:
        print('No')
    else:
        print('Yes')
        
def is_triangle1():
    a = input('Input length 1:')
    b = input('Input length 2:')
    c = input('Input length 3:')
    is_triangle(a, b, c)





# Test code
is_triangle(3,4,5)
is_triangle1()
