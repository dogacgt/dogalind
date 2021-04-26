#!/usr/bin/env python
#Counting Subsets

with open('data/rosalind_sset.txt', 'r') as f:
    n = int(f.read().strip())

print(2**n % 1_000_000)
