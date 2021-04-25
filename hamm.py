#!/usr/bin/env python
#Counting Point Mutations

with open('data/rosalind_hamm.txt', 'r') as f:
    s, t = f.read().strip().split()

n = len(s)
d = 0
for i in range(n):
    if s[i] != t[i]:
        d += 1
print(d)
