#!/usr/bin/env python
#Mendel's First Law

with open('data/rosalind_iprb.txt') as f:
    k, m, n = map(int, f.read().strip().split())
    t = k+m+n

res = (k*(k-1)+(2*k*m)+(2*k*n)+.75*m*(m-1)+(m*n))/(t*(t-1))
print('%.5f'%(res))
