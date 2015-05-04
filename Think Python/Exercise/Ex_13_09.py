# Rank of a word
import matplotlib.pyplot as plt
from math import log

def get_hist(file_name):
    fin = open(file_name)
    word_freq = {}
    for line in fin:
        for w in line.split():
            w = w.strip()
            if w in word_freq.keys():
                word_freq[w] += 1
            else:
                word_freq[w] = 1
    return word_freq

def rank_word(word_freq):
    t = []
    logf = []
    logr = []
    total_num = sum(list(word_freq.values()))
    for key, value in word_freq.items():
        t.append((value/total_num, key))
    t.sort(reverse=True)
    for i, t in enumerate(t):
        logf.append(log(t[0]))
        logr.append(log(i+1))
    plt.plot(logf, logr)
    plt.show()
        

# Test code
w_freq = get_hist('Ex_13_08_pg158.txt')
rank_word(w_freq)
    
    
        
    