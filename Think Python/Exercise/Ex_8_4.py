# modify find so that it has a third parameter

def find(word, letter, index):
    '''
    find the letter in the word, starting from the index in the word
    '''
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1



# Test code
print(find('Samuel', 'a', 0))