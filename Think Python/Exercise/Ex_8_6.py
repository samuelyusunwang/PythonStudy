# using find() to count the letter in a word

from Ex_8_4 import find

def count1(word, letter):
    N = len(word)
    count = 0
    
    i = 0
    while i <= N-1:
        idx = find(word[i:], letter, i)
        if idx == -1:
            break
        else:
            count = count + 1
            i = idx + 1
    return count




# Test code
print(count1('abcdabcdab', 'e'))