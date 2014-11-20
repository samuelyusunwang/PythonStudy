# convert word.txt to a list and compare the speed

# method 1: use append()
def word2ListV1(filename):
    fin = open(filename)
    t = []
    for word in fin:
        word = word.strip()
        t.append(word)
    return t

def word2ListV2(filename):
    fin = open(filename)
    t = []
    for word in fin:
        t = t + [word]
    return t

