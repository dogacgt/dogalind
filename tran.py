#!/usr/bin/python
#Transitions and Transversions

from Bio import SeqIO

with open('data/rosalind_tran.txt', 'r') as f:
    s1, s2 = SeqIO.parse(f, 'fasta')
    s1, s2 = s1.seq, s2.seq

pur, pyr = ['A', 'G'], ['C', 'T']

transition = 0
transversion = 0
for i in range(len(s1)):
    if s1[i] == s2[i]:
        continue
    if (s1[i] in pur and s2[i] in pur) or (s1[i] in pyr and s2[i] in pyr):
        transition += 1
    if (s1[i] in pur and s2[i] in pyr) or (s1[i] in pyr and s2[i] in pur):
        transversion += 1

print(transition/transversion)
