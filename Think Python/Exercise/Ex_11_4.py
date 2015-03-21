# Modify reverse_lookup so that it returns a list of all keys that map to v,
# or an empty list if there are none

def reverse_lookup(d, v):
    l = list()
    for k in d:
        if d[k] == v:
            l.append(k)
    return l


# Test code
from Ex_11_2 import histograms1

d = histograms1('abcabcdklsjfoiwhrghahfoweruiqwhr')
print(d)

k = reverse_lookup(d, 1)

print(k)