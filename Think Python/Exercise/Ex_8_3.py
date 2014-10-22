# abecedarian series

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter != 'O' and letter != 'Q':
        print(letter + suffix)
    else:
        print(letter + 'u' + suffix)
        

