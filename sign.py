#!/usr/bin/env python
#Enumerating Oriented Gene Orderings

from itertools import permutations, product

with open('data/rosalind_sign.txt') as f:
    n=int(f.read().strip())

iterable = range(1, n+1)

L = []
for perm in permutations(iterable):
    for i in product(*[[-p, p] for p in perm]):
        L.append(i)

with open('output.txt', 'w') as f:
    f.write(str(len(L))+'\n')
    for item in L:
        f.write(' '.join(map(str, item)) + '\n')
