# Car TAlk Puzzle: Homophone

from Ex_11_1 import *

from pronounce import *

dict_pronounce = read_dictionary()

for word in word_dict:
    if len(word) == 6:
        word1 = word[1:]
        word2 = list(word)
        word2.pop(1)
        word2 = ''.join(word2)
        if word1 in dict_pronounce.keys() and word2 in dict_pronounce.keys():
            pronounce1 = dict_pronounce[word1]
            pronounce2 = dict_pronounce[word2]
            if pronounce1 == pronounce2:
                print(word, word1, word2)


