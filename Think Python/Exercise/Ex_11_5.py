# concise version of invert_dict

def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
#         if val not in inv:
#             inv[val] = [key]
#         else:
#             inv[val].append(key)
        inv.setdefault(val, list())
        inv[val].append(key)
    return inv


# Test code
from Ex_11_2 import histograms1

d = histograms1('abcabcdklsjfoiwhrghahfoweruiqwhr')
print(d)

inv_d = invert_dict(d)
print(inv_d)