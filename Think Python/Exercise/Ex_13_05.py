# choose_from_hist(): choose randomly based on histogram

import random

def choose_from_hist(hist):
    total = sum(hist.values())
    cum_prod = 0
    x = random.random()
    for (key, val) in hist.items():
        cum_prod += val/total
        if x < cum_prod:
            return key


# Test code
d = dict(zip('abcde', range(5)))
for i in range(20):
    print(choose_from_hist(d))
