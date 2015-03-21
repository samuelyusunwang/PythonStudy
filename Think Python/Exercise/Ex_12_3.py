# Letter Frequency

def most_frequent(s):
    hist = dict()
    for letter in s:
        if letter in hist.keys():
            hist[letter] += 1
        else:
            hist[letter] = 1
    hist_sort = []
    for x, freq in hist.items():
        hist_sort.append((freq, x))
    hist_sort.sort(reverse=True)
    for freq, x in hist_sort:
        print(x, freq)
    
    
# Test code
s = 'abcdefgskfiahfndabnfuherwkwbefsdf'
most_frequent(s)