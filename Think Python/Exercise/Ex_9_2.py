# Ex 9.2 has_no_e()

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True


# Test code
fin = open('words.txt')

for line in fin:
    word = line.strip()
    if has_no_e(word):
        print(word)