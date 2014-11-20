# rewrite the histogram() more concisely

def histograms(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histograms1(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

# Test code
print(histograms('ababcdeffff'))
print(histograms1('ababcdeffff'))