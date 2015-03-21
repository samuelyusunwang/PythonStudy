# Using dictionary to implement the has_duplicate function

def has_duplicates_dict(x):
    d = histograms(x)
    for key in d:
        if d[key] > 1:
            return True
    return False
    
def histograms(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# Test code
x = [1, 2, 3, 4, 5, 5]
print(has_duplicates_dict(x))

y = [0, 1, 2, 3, 4, 5]
print(has_duplicates_dict(y))