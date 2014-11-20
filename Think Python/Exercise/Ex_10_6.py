# Remove duplicates

def remove_duplicates(t):
    t_unique = []
    for x in t:
        if x not in t_unique:
            t_unique.append(x)
    return t_unique


# Test code
t = [1,2,3,1,2,3,99]
print(remove_duplicates(t))

t = ['xx','yy','x','yy','xyz','yx']
print(remove_duplicates(t))