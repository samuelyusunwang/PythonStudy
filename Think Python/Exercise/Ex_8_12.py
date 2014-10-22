# ROT13 encryption

def rotate_word(s, position):
    l = []
    for letter in s:
        x = ord(letter) + position
        if letter.islower():
            x = (x-ord('a'))%(ord('z')-ord('a')+1) + ord('a')
        else:
            x = (x-ord('A'))%(ord('Z')-ord('A')+1) + ord('A')
        l.append(chr(x))
    return ''.join(l)


# Test
print(rotate_word('cheer',7))
print(rotate_word('melon', -10))

print(rotate_word('CHEer',7))
print(rotate_word('MELon', -10))