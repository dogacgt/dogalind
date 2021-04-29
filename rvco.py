#!/usr/bin/env python
#Complementing a Strand of DNA

from Bio import SeqIO

dnas = SeqIO.parse('data/rosalind_rvco.txt', 'fasta')

c = 0
for dna in dnas:
    if dna.seq == dna.reverse_complement().seq:
        c += 1

print(c)
