# Birthday Paradox
# Simulate birthdays and checking for matches

import numpy as np

def birthdayMatchProb(N):
    # Generate T samples of N random integers to mimic the birthdays
    Match = 0
    nTrial = 10000
    x = np.random.randint(1,360, size=(N,nTrial) )
    for i in range(nTrial):
        if has_duplicates(x[:,i]):
            Match = Match + 1
    return Match/nTrial

def has_duplicates(x):
    x_sorted = x
    x_sorted.sort()
    N = len(x_sorted)
    for i in range(N-1):
        if x_sorted[i] == x_sorted[i+1]:
            return True
    return False


# Test code
n = [5, 10, 20, 23, 30, 40, 50, 60]
for i in n:
    print(i,': ',birthdayMatchProb(i))
