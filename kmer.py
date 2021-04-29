#!/usr/bin/env python
#k-Mer Composition

import re
import itertools

def kmer_comp():
    kmer = {}
    pros = itertools.product('ACGT', repeat=4)
    for pro in pros:
        x = ''.join(pro)
        if x not in kmer:
            kmer[x] = 0

    with open('output.txt', 'w') as f:
        for key in kmer.keys():
            c = len(re.findall(r'(?={0})'.format(key), s))
            f.write('{} '.format(str(c)))

if __name__ == '__main__':
    with open('data/rosalind_kmer.txt') as f:
        s = ''
        for line in f.readlines():
            if line[0] != '>':
                s += line.strip()
    kmer_comp()
