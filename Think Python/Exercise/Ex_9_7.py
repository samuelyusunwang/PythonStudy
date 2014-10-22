# Three consecutive double letters

def find3Doubles(word):
    word = word.lower()
    N = len(word)
    if N < 6:
        return False
    else:
        i = 0
        while i <= N-6:
            if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
                return True
            else:
                i = i + 1
        return False
    

# test code
print(find3Doubles('aabbcc'))

fin = open('words.txt')

for line in fin:
    word = line.strip()
    if find3Doubles(word):
        print(word)
        