# Ex 3.4
# print string that the last letter is in the column 70 of display

def right_justify(s):
    nSpace = 70 - len(s)
    print(' ' * nSpace + s)
    
# test
right_justify('Allen')
print(' ')
##########################################

# Ex 3.4
# do four?

def print_twice(s):
    print(s)
    print(s)
    
def do_twice(f, s):
    f(s)
    f(s)

def do_four(f, s):
    do_twice(f, s)
    do_twice(f, s)

# test
do_twice(print_twice, 'Spam')
print(' ')
do_four(print_twice, 'Spam')
print(' ')
##################################################

# Ex 3.5 Print Fancy stuff
s1 = '+----+----+'
s2 = '|    |    |'
print(s1)
do_twice(print_twice, s2)
print(s1)
do_twice(print_twice, s2)
print(s1)
#################################################





 