# Car Talk Puzzle: reversed age digit problem

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    N = len(word1)
    i = 0
    while i <= N-1:
        if word1[i] != word2[N-1-i]:
            return False
        i = i + 1
    return True

def getReverseAge(birthAge):
    ageSon = 0
    ageMom = birthAge
    while ageMom < 99:
        if is_reverse(str(ageSon), str(ageMom)):
            print('BirthAge:', birthAge, 'SonAge', ageSon, 'MomAge', ageMom)
        ageMom = ageMom + 1
        ageSon = ageSon + 1
        
# Test code
print(is_reverse('21', '13'))

for x in range(16,40):
    getReverseAge(x)