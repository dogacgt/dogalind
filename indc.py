#!/usr/bin/python3
#Independent Segregation of Chromosomes

from math import factorial, log

with open('data/rosalind_indc.txt') as f:
    n = int(f.read().strip())

arr = [0]*(n*2)
#common log: log_10(probability)

def binomDist(n, arr):
    ind = 2 * n
    binom = 0
    sharingChr = 1/(ind)
    for i in range(ind, 0, -1):
        binom += C(ind, i) * (.5 ** (ind))
        arr[i-1] = binom
    arr = [log(x, 10) for x in arr]

    with open('output.txt', 'w') as f:
        arr = ['%.4f' % a for a in arr]
        f.write(' '.join(map(str, arr)))

def C(m, r):
    return factorial(m)/(factorial(m-r) * factorial(r))

binomDist(n, arr)
