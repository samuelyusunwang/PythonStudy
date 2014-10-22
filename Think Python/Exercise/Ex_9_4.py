# Check if the word only uses the allowed letters

def use_only(word, candidates):
    for letter in word:
        idx = candidates.find(letter)
        if idx == -1:
            return False
    return True


# Test code
fin = open('words.txt')
candidates = input('Input the allowed words:')

for line in fin:
    word = line.strip()
    if use_only(word, candidates):
        print(word)