# cumulative sum

def cum_sum(x):
    sum = 0
    res = []
    for k in x:
        sum += k
        res.append(sum)
    return res


# Test code
x = range(1,10)
print(x[:])
print(cum_sum(x))