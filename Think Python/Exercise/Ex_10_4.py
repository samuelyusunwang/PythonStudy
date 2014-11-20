# determine if a word is an anagram of the other
# i.e. the letters in one word can be rearranged to form the other

def is_anagram(word1, word2):
    t1 = list(word1)
    t2 = list(word2)
    t1.sort()
    t2.sort()
    return t1 == t2


# Test
print(is_anagram('abcd', 'dbac'))
print(is_anagram('sam','tom'))