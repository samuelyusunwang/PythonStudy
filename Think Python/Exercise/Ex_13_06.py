# use set operation to subtract words in the book that are not in the word list

import string

# COPY from Ex_13_04
def count_words(file_name):
    fin = open(file_name)
    # Get the words
    words = []
    mainbody_flag = False
    for line in fin:
        if line == 'End of Project Gutenberg''s Around the World in 80 Days, by Jules Verne\n':
            break
        elif line == '*** START OF THIS PROJECT GUTENBERG EBOOK AROUND THE WORLD IN 80 DAYS ***\n':
            mainbody_flag = True
            continue
        if mainbody_flag:  
            temp_list = line.split()
            for w in temp_list:
                w.strip()
                trans_tbl = str.maketrans('','',string.punctuation)
                w = w.translate(trans_tbl)
                w = w.lower()
                words.append(w)    
    # Get the histogram of the words
    hist = {}
    for w in words:
        if w in hist.keys():
            hist[w] += 1
        else:
            hist[w] = 1
    return len(hist.keys()), hist


# Test Main Code 
# Get words from a book
(total_num_words, hist) = count_words('Ex_13_02_pg103.txt')
words_book = set(hist.keys())

# Get words from word_list
fin = open('words.txt')
words = []
for line in fin:
    words.append(line.strip())
words_list = set(words)

# subtract words_list from words_book
words_typo = words_book - words_list
print('Here are the words from the book that are not in the word list')
for w in words_typo:
    print(w)




