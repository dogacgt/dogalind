#!/usr/bin/env python
#Independent Alleles

#binomial distribution, because we have two categories, being AaBb and not.
## P(AaBb) = 0.25 always

def LIA(k, N):
    ind = 2 ** k
    binom = 0
    for i in range(N, ind+1):
        binom += C(ind, i) * (.25**i) * (.75**(ind-i))
    return '%.3f' %binom

def C(n, r): #combination
    return F(n) / (F(n-r) * F(r))

def F(num): #factorial
    if num == 0: return 1
    return num * F(num-1)

if __name__ == '__main__':
    with open('data/rosalind_lia.txt', 'r') as f:
        k, N = map(int, f.read().strip().split())
        print(LIA(k, N))
