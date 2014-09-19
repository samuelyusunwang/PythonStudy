# Ex 3.1 & 3.2 : Call function before its definition

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm fine")
    print("I'm very fine")



repeat_lyrics()
