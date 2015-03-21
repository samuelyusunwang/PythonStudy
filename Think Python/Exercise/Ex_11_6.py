# Compare fibonacci() with and without memo

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

def fibonacci_old(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_old(n-1)+fibonacci_old(n-2)


# Test code
print(fibonacci(20))
print(fibonacci_old(20))