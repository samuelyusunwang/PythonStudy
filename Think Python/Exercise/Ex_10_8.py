# Use bisect (binary search) method to check whether a word is in the word list

from Ex_10_7 import word2ListV1

def bisect(target, sortedList):
    Start = 0
    End = len(sortedList)
    Mid = round(End/2)
    while Start < End-1:
        if target < sortedList[Mid]:
            End = Mid
            Mid = round((Start+End)/2)
        else:
            Start = Mid
            Mid = round((Start+End)/2)
    if target == sortedList[Start]:
        return Start
    elif target == sortedList[End]:
        return End
    else:
        return None
    
    
# Test code
# words = ['a','b','c','d','e','f','g']
# print(bisect('x',words))

words = word2ListV1('words.txt')
print(bisect('jack', words))


        
        
        