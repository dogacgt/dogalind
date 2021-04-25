#!/usr/bin/python3
#Perfect Matchings and RNA Secondary Structures

from math import factorial

with open('data/rosalind_pmch.txt', 'r') as f:
    s = ''
    for line in f.readlines():
        if line[0] != '>':
            s += line.rstrip('\n')

au = s.count('A')
gc = s.count('G')

print(factorial(gc) * factorial(au))
