# Compare one word is the reverse of the other

def is_reverse(word1, word2):
    '''
    Test debugging
    '''
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2) - 1
    
    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    
    return True



# Test code
print(is_reverse('spot', 'tops'))