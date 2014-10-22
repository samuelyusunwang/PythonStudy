# Check if the word doesn't use any of the forbidden letters

def avoid(word, forbidden):
    for letter in forbidden:
        idx = word.find(letter)
        if idx != -1:
            return False
    return True


# Test code
fin = open('words.txt')
forbidden = input('Input the forbidden letters:')

for line in fin:
    word = line.strip()
    if avoid(word, forbidden):
        print(word)