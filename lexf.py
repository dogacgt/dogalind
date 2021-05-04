#!/usr/bin/env python
#Enumerating k-mers Lexicographically

from itertools import product

with open('data/rosalind_lexf.txt') as f:
    f = f.readlines()
    perm = f[0].strip().split()
    n = int(f[1].strip())

result = product(perm, repeat=n)

with open('output.txt', 'w') as f:
    for item in result:
        str = ''
        for num in item:
            str += num
        f.write(str + '\n')
