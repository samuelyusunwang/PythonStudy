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

#1. 
fin = open('words.txt')
anagrams_dict = dict()
for line in fin:
    word = line.strip()
    h = hist(word)
    if tuple(h.items()) in anagrams_dict.keys():
        anagrams_dict[tuple(h.items())].append(word)
    else:
        anagrams_dict[tuple(h.items())] = [word]

#2. 
summary = []
for key, val in anagrams_dict.items():
    if len(val) > 1:
        summary.append((len(key),key,val))
summary.sort(reverse=True)

for i in range(0,3):
    print(summary[i])

# 3. Bingo with 8 letters
max_possible_bingo = 0
for n, key, val in summary:
    if n == 8:
        if len(val) > max_possible_bingo:
            val_max = val
            max_possible_bingo = len(val)
print(val_max)
        

#4.  metathesis pair
for n, h, words in summary:
    if n > 1:
        K = len(words)
        for i in range(K):
            for j in range(i+1,K):
                count = 0
                for l in range(len(words[i])):
                    count += words[i][l]!=words[j][l]
                if count == 2:
                    print(words[i], words[j])

            
        







    