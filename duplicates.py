import hashlib
import collections

i = 0

d = collections.defaultdict(list)
with open('test_data.txt', 'r') as datafile:
    for line in datafile:
        
        id = hashlib.sha256(line.encode()).digest()
        # Or id = line[:n]
        k = id[0:2]
        v = id[2:]
        if v in d[k]:
            print("double found:", id, "in line: ", line, i)
        else:
            d[k].append(v)
        
        i = i + 1 
