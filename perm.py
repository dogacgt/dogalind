#!/usr/bin/env python
#Enumerating Gene Orders

import itertools
import math

def main():
    iterable = range(1, n+1)
    with open('output.txt', 'w') as f:
        f.write(str(math.factorial(n)) + '\n')
        result = itertools.permutations(iterable, n)
        for item in result:
            f.write(' '.join(map(str, item)) + '\n')

if __name__ == '__main__':
    with open('data/rosalind_perm.txt') as f:
        n = int(f.read().strip())
        main()
