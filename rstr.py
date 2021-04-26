#!/usr/bin/env python
#Matching Random Motifs

with open('data/rosalind_rstr.txt') as f:
    N, s = f.readline().strip().split()
    N, s = int(N), float(s)
    dna = str(f.readline().strip())

prob_gc = s / 2
prob_at = .5 - prob_gc

total_prob = 1
total_prob = prob_at ** (dna.count('A') + dna.count('T'))
total_prob *= prob_gc ** (dna.count('G') + dna.count('C'))

print('%.3f' % float(1-(1-total_prob)**N))
