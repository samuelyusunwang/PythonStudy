# Solve the car talk puzzler of palindromic odometers

def is_palindromic(word):
    N = len(word)
    i = 0
    while i < (N-1)/2:
        if word[i] != word[N-1-i]:
            return False
        i = i + 1
    return True


# Test code
print(is_palindromic('12321'))

print(is_palindromic('1001'))        
        
# Find the number
x = 100000
while x <= 999999:
    temp = str(x)
    if is_palindromic(temp[-4:]):
        temp = str(x+1)
        if is_palindromic(temp[-5:]):
            temp = str(x+2)
            if is_palindromic(temp[1:4]):
                temp = str(x+3)
                if is_palindromic(temp):
                    print(x, x+1, x+2, x+3)
    x = x + 1
