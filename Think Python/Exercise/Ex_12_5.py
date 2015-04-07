# Longest English Word

def get_children(word, word_list):
    if word not in word_list:
        return []
    else:
        children = []
        for i in range(len(word)):
            w = ''.join([word[0:i],word[i+1:]])
            if w in word_list:
                children.append(w)
        return children

def is_reducible(word, word_list, reducible_list):
    if word not in word_list:
        return (False, [])
    elif word in reducible_list:
        return (True, [])
    elif word == 'I' or word == 'a' or word == '':
        return (True, [])
    elif word == []:
        return (False, [])
    else:
        children = get_children(word, word_list)
        for w in children:
            w_tag, w_children = is_reducible(w, word_list, reducible_list)
            if not w_tag:
                return (False, [])
        if children == []:
            return (False, [])
        else:
            return (True, children)
    

   
    
# Test Code
fin = open('words_ex_12_5.txt')
word_list = []
for line in fin:
    w = line.strip()
    word_list.append(w)

#1. Test getChildren()
print(get_children('sprite',word_list))

#2. Test is_reducible()
# print(is_reducible('a', word_list, []))
# print(is_reducible('sprite', word_list, []))
# print(is_reducible('Sex', word_list, []))

# print(is_reducible('counterdemonstration', word_list, []))
print(get_children('aardvarks', word_list))
print(is_reducible('aardvarks', word_list, ['','I','aa','aah','ah','aahs','aas','aal','aaliis','aalii','aals']))

#3. Find the longest word
len_longest = 0
word_longest = ''
reducible_list = []
for word in word_list:
    if len(word) < len_longest:
        continue
    reducible_flag, children = is_reducible(word, word_list, reducible_list)
    if reducible_flag:
        if word not in reducible_list:
            reducible_list.append(word)
        for w in children:
            if w not in reducible_list:
                reducible_list.append(w)
        if len(word) > len_longest:
            word_longest = word
            len_longest = len(word_longest)
            print(word_longest, len_longest)
              
print('Longest Word:', word_longest)
         









