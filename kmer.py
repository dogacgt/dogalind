#!/usr/bin/env python
#k-Mer Composition

import re
import itertools

with open('data/rosalind_kmer.txt') as f:
    f = f.readlines()
    s = ''
    for line in f:
        if line[0] != '>':
            s += line.strip()

dict = {}
pros = itertools.product('ACGT', repeat=4)
for pro in pros:
    x = ''.join(pro)
    if x not in dict:
        dict[x] = 0

with open('output.txt', 'w') as f:
    for key in dict.keys():
        c = len(re.findall(r'(?={0})'.format(key), s))
        f.write(str(c) + ' ')
