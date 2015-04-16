# 1. Reads a file
# 2. Breaks each line into words
# 3. strips whitespace and punctuations
# 4. converts them to lowercase

import string

def process_file(file_name):
    fin = open(file_name)
    words = []
    for line in fin:
        temp_list = line.split()
        for w in temp_list:
            w.strip()
            trans_tbl = str.maketrans('','',string.punctuation)
            w = w.translate(trans_tbl)
            w = w.lower()
            words.append(w)
    return words
        

# Test file
words = process_file('Ex_13_01_test.txt')
print(words)