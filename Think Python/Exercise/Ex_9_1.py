# Reads words.txt and prints only the words with more than 20 characters (whitespace excluded)

fin = open('words.txt')

for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)


        