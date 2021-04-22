#!/usr/bin/python3
#Maximum Matchings and RNA Secondary Structures

from math import factorial

def C(n, r):
    return factorial(n) // factorial(n-r)

with open('data/rosalind_mmch.txt', 'r') as f:
    s = ''
    for line in f.readlines():
        if line[0] != '>':
            s += line.rstrip('\n')

aux, aun = max(s.count('A'), s.count('U')), min(s.count('A'), s.count('U'))
gcx, gcn = max(s.count('G'), s.count('C')), min(s.count('G'), s.count('C'))

print(C(aux, aun) * C(gcx, gcn))
