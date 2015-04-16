# Check if the words of a book are in the word list

import string

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
(total_num_words, hist) = count_words('Ex_13_02_pg103.txt')
words_book = hist.keys()

fin = open('words.txt')
words = []
for line in fin:
    words.append(line.strip())
words_typo = []
for w in words_book:
    if w not in words:
        words_typo.append(w)
print(words_typo)
    


