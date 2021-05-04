#!/usr/bin/env python
#Consensus and Profile

from Bio import SeqIO

seqs=[]
for record in SeqIO.parse('data/rosalind_cons.txt', 'fasta'):
    seqs.append(str(record.seq))

def profile(seqs, letter):
    length = len(seqs[0])
    count = [0] * length
    for i in range(length):
        for seq in seqs:
            if seq[i] == letter:
                count[i] += 1
    return count

A = profile(seqs, 'A')
G = profile(seqs, 'G')
C = profile(seqs, 'C')
T = profile(seqs, 'T')

def consensus():
    cons = ''
    for i in range(len(A)):
        hi = max(A[i], G[i], C[i], T[i])
        if hi == A[i]: cons += 'A'
        elif hi == G[i]: cons += 'G'
        elif hi == C[i]: cons += 'C'
        elif hi == T[i]: cons += 'T'
    return cons

with open('output.txt', 'w') as f:
    f.write('{}\n'.format(consensus()))
    f.write('A: {}\n'.format(' '.join(map(str, A))))
    f.write('C: {}\n'.format(' '.join(map(str, C))))
    f.write('G: {}\n'.format(' '.join(map(str, G))))
    f.write('T: {}'.format(' '.join(map(str, T))))
