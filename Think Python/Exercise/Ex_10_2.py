# chop the 1st and last elts in a list

def chop(t):
    t.pop(0)
    t.pop(-1)

def middle(t):
    return t[1:-1]

# Test code
t1 = [1, 2, '3', 4, '5']
t2 = [1, 2, '3', 4, '5']

chop(t1)
print(t1)

print(middle(t2))