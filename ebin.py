#!/usr/bin/env python

with open('data/rosalind_ebin.txt') as f:
    n, *P = [float(i) for i in f.read().strip().split()]

with open('output.txt', 'w') as f:
    arr = [round(n*prob, 3) for prob in P]
    f.write(' '.join(map(str, arr)))

