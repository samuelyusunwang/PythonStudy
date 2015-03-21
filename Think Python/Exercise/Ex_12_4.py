# More anagrams

# get hist of the letters
def hist(word):
    h = dict()
    for letter in word:
        if letter in h.keys():
            h[letter] += 1
        else:
            h[letter] = 1
    return h

   

# Test code
h = hist('abcdsfjasld')
print(h)

fin = open('words.txt')
anagrams_dict = dict()
for line in fin:
    word = line.strip()
    h = hist(word)
    if tuple(h.items()) in anagrams_dict.keys():
        anagrams_dict[tuple(h.items())].append(word)
    else:
        anagrams_dict[tuple(h.items())] = [word]

summary = []
for key, val in anagrams_dict.items():
    summary.append((len(val),key,val))
summary.sort(reverse=True)

for i in range(0,3):
    print(summary[i])

# Bingo with 8 letters
for n, key, val in summary:
    if n == 8:
        print(val)

# metathesis pair
for n, h, words in summary:
    if n > 1:
        for w in words:
            
        







    