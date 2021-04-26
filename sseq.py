#!/usr/bin/env python
#Finding a Spliced Motif

from Bio import SeqIO

with open('data/rosalind_sseq.txt') as f:
    dna = []
    for record in SeqIO.parse(f, 'fasta'):
        dna.append(record.seq)
    s, t = dna[0], dna[1]

memo = [0]*len(t)

for i in range(len(t)):
    if i-1 >= 0:
        memo[i] = s[memo[i-1]:].find(t[i]) + memo[i-1] + 1
    else:
        memo[i] = s.find(t[i]) + 1

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, memo)))
