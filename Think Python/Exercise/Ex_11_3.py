# print the items in a dictionary in alphabetical order

def print_alp(h):
    x = h.keys()
    x = list(x)
    x.sort()
    for c in x:
        print(c, h[c])


# Test code
from Ex_11_2 import histograms1

d = histograms1('abcabcdklsjfoiwhrghahfoweruiqwhr')

print_alp(d)