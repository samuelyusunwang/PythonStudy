# check if two words are reverse pair of each other

from Ex_10_7 import word2ListV1

words = word2ListV1('words.txt')
N = len(words)
for i in range(N):
    if words[i][::-1] in words[i+1:]:
        print(words[i], words[i][::-1])



        