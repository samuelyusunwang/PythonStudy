# determine whether a list is sorted

def is_sorted(t):
    N = len(t)
    for i in range(N-1):
        if t[i] > t[i+1]:
            return False
    return True


# Test
print(is_sorted([1,2,5,7]))
print(is_sorted(['a','be','cd']))
print(is_sorted([2,1,0,5]))