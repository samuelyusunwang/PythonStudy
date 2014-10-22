# Check if the word is in alphabetical order

def is_abecedarian(word):
    word = word.lower()
    N = len(word)
    for i in range(N-1):
        if word[i] > word[i+1]:
            return False
    return True


# Test code
fin = open('words.txt')

for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        print(word)
        
        