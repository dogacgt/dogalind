#!/usr/bin/env python
#Introduction to Alternative Splicing

from math import factorial as fact

def void():
    result = 0
    for k in range(m, n+1):
        result += fact(n) // (fact(n-k) * fact(k))
    return result % 10**6

if __name__ == '__main__':
    with open('data/rosalind_aspc.txt', 'r') as f:
        n, m = map(int, f.read().strip().split())
        print(void())
