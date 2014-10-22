# count

def count(word, letter):
    '''
    count the number of letter in word
    '''
    count = 0
    for x in word:
        if x == letter:
            count = count + 1
    return count


# test code
print(count('abcdabcda', 'a'))