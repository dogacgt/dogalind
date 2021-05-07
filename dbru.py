#!/usr/bin/env python
#Constructing a De Bruijn Graph

def rev_comp(s):
    t=''
    dna_dict={'A':'T','T':'A','G':'C','C':'G'}
    for i in s:
        t+=dna_dict[i]
    return t[::-1]

def de_bruijn(s, k):
    return '({}, {})'.format(s[:k],s[1:k+1])

with open('data/rosalind_dbru.txt') as f:
    S = f.read().strip().split()
    k = len(S[0])-1
    S = S + [rev_comp(s) for s in S]

    nodes = []
    for s in S:
        if s not in nodes:
            nodes.append(s)
    nodes.sort()

with open('output.txt', 'w') as f:
    for node in nodes:
        f.write('%s\n' % de_bruijn(node, k))
