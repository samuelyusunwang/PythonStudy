# store the words as keys in a dictionary

fin = open("words.txt")

word_dict = dict()
for word in fin:
    word = word.strip()
    word_dict[word] = ''

print('jack' in word_dict)