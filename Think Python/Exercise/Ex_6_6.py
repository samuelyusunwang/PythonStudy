# Ex 6.6 Palindrome

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    '''
    Use Recursion to find if the word is palindrome
    '''
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    elif first(word) == last(word):
        return is_palindrome(word[1:-1])
    

# Test code
print(is_palindrome('XYZZYX'))
print(is_palindrome('a'))
    

