#!/usr/bin/env python
#Degree Array

with open('data/rosalind_deg.txt', 'r') as f:
    res = list(map(int, f.read().strip().split()))

with open('output.txt', 'w') as f:
    for i in range(1, res[0]+1):
        f.write('{} '.format(str(res[2:].count(i))) )
