# Create a dictionary that maps from prefixes to a collection of possible suffixes
import random

# 1. get mapping from a book
def get_mapping(file_name, len_prefix):
    fin = open(file_name)
    words = []
    for line in fin:
        temp_list = line.split()
        for w in temp_list:
            # words.append(w.strip())
            words.append(w) 
    N = len(words)
    mapping_hist = dict()
    for i in range(N-len_prefix):
        prefix = words[i:i+len_prefix]
        surfix = words[i+len_prefix]
        prefix = tuple(prefix)
        surfix = (surfix,)
        # store surfix in the form of a dictionary
        if prefix not in mapping_hist.keys():
            mapping_hist[prefix] = {surfix: 1}
        elif surfix not in mapping_hist[prefix].keys():
            mapping_hist[prefix][surfix] = 1
        else:
            mapping_hist[prefix][surfix] += 1
    return mapping_hist


# 2. generate random text
def random_text(mapping, len_sentence=30):
    words = []
    prefix_hist = dict()
    for prefix, surfix in mapping.items():
        prefix_hist[prefix] = sum( list(surfix.values()) )
    prefix = choose_from_hist(prefix_hist)
    words.extend(prefix)
    while len(words) < len_sentence:
        prefix = tuple(words[-2:])
        if prefix in mapping.keys():
            surfix = choose_from_hist(mapping[prefix])
            words.extend(surfix)
        else:
            words.extend( choose_from_hist(prefix_hist) )
    return words

        
        
        
# Define new most common prefix
def most_common_prefix(h):
    t = []
    for key, value in h.items():
        N = len(value.keys())
        t.append((N, key, value.keys()))
    t.sort(reverse=True)
    return t

# Randomly Select the key from a histogram
def choose_from_hist(hist):
    total = sum(list(hist.values()))
    cum_prod = 0
    x = random.random()
    for (key, val) in hist.items():
        cum_prod += val/total
        if x < cum_prod:
            return list(key)


# Test code get mapping
m_hist1 = get_mapping('Ex_13_02_pg103.txt', 2)

m_tuple = most_common_prefix(m_hist1)
print('The most common prefix')
for freq, prefix, surfix in m_tuple[0:3]:
    print(prefix, '\t', freq, '\t', surfix)
    
# Test code for random text
print('Random Text 1: Prefix Length = 2')
rand_list = random_text(m_hist1)
print(' '.join(rand_list, ))


# Test code for different length of prefix
m_hist2 = get_mapping('Ex_13_02_pg103.txt', 5)
print('Random Text 2: Prefix Length = 5')
rand_list = random_text(m_hist2)
print(' '.join(rand_list, ))

# Add a different book
m_hist3 = get_mapping('Ex_13_08_pg158.txt', 2)
m_hist_combine = {}
for key, value in m_hist1:
    m_hist_combine[key] = value
for key, value in m_hist3:
    m_hist_combine[key] = value
print('Random Test 3: Two books combined')
rand_list = random_text(m_hist3)
print(' '.join(rand_list, ))



