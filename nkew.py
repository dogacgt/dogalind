#!/usr/bin/env python
#Newick Format with Edge Weights

from Bio import Phylo
from io import StringIO

with open('data/rosalind_nkew.txt') as f:
    f = f.readlines()
    T = []
    i = 0
    while i <= len(f):
        nwk = f[i].strip()
        x, y = f[i+1].strip().split()
        handle = StringIO(nwk)
        tree = Phylo.read(handle, 'newick')
        T.append(int(tree.distance(x, y)))
        i += 3

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, T)))
