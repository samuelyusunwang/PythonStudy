# Print top 20 most frequently-used words

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
    # sort the words based on frequency
    t = []
    for key, val in hist.items():
        t.append((val,key))
    t.sort(reverse=True)
    output = []
    for val, key in t[0:20]:
        output.append((key, val))
    return output
        


# Test code
output = count_words('Ex_13_02_pg103.txt')
for w in output:
    print(w[0], w[1])






