#!/usr/bin/env python
#Counting Unrooted Binary Trees

with open('data/rosalind_cunr.txt') as f:
    n = int(f.read().strip())

#double factorial
def dfact(n):
    if n<2: return 1
    return n * dfact(n-2)

print(dfact(n)%10**6)
