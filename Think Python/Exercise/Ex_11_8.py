# Rotate Pairs
from Ex_10_7 import word2ListV1

def get_dict_mapping(position):
    dict_mapping = dict()
    
    for x in range(ord('a'),ord('z')+1):
        y = x + position
        dict_mapping[chr(x)] = chr( (y-ord('a'))%(ord('z')-ord('a')+1) + ord('a') )
        
    for x in range(ord('A'),ord('Z')+1):
        y = x + position
        dict_mapping[chr(x)] = chr( (y-ord('A'))%(ord('Z')-ord('A')+1) + ord('A') )
        
    return dict_mapping

def rotate_word(s, position):
    d = get_dict_mapping(position)
    s_rotate = []
    for x in s:
        s_rotate.append(d[x])
    return ''.join(s_rotate)
    
    
    
# Test code
d = get_dict_mapping(-1)
for i in range(ord('a'), ord('z')+1):
    print(d[chr(i)], end="")
    
print()
s = 'Sam'
print(rotate_word(s,3))

# Find all the words that are rotated
words = word2ListV1('words.txt')
pos = 10
for w in words:
    w_rotate = rotate_word(w,pos)
    if rotate_word(w,pos) in words:
        print(w, w_rotate)






 
