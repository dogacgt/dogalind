#!/usr/bin/python3
#Independent Segregation of Chromosomes

from math import factorial, log
#common log: log_10(probability)

def binom_dist(n):
    arr = [0]*(n*2)
    ind = 2 * n
    binom = 0
    for i in range(ind, 0, -1):
        binom += C(ind, i) * (.5 ** (ind))
        arr[i-1] = binom
    arr = [log(x, 10) for x in arr]

    with open('output.txt', 'w') as f:
        arr = ['%.4f' % a for a in arr]
        f.write(' '.join(arr))

def C(m, r):
    return factorial(m)/(factorial(m-r) * factorial(r))

if __name__ == '__main__':
    with open('data/rosalind_indc.txt') as f:
        n = int(f.read().strip())
    binom_dist(n)
