# check interlock words

from Ex_10_7 import word2ListV1

words = word2ListV1('words.txt')

# interlock
# for w in words:
#    if w[0::2] in words and w[1::2] in words:
#       print(w, w[0::2], w[1::2])

# three-way interlock
for w in words:
    if w[0::3] in words and w[1::3] in words and w[2::3] in words:
        print(w, w[0::2], w[1::2], w[2::3])