# Check if all the required words are used

def use_all(word, candidates):
    for letter in candidates:
        if letter not in word:
            return False
    return True


# Test code
fin = open('words.txt')
candidates = input('Input the required words:')

for line in fin:
    word = line.strip()
    if use_all(word, candidates):
        print(word)
        