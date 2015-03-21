# sort by length; random order of the words with the same length
import numpy as np

def sort_by_length(words):
    t = []
    for x in words:
        t.append((len(x), np.random.randn(), x))
    t.sort(reverse=True)
    
    res = []
#     for length, rank, word in t:
#         res.append(word)
    for k in t:
        res.append(k[-1])
    return res


# Test code
word_list = ['abc', 'acb', 'bca', 'cdf', 'dkflsjf', 'dksfljdd']
test = sort_by_length(word_list)
print(test) 