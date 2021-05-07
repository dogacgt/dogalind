#!/usr/bin/env python
#Base Filtration by Quality

from Bio import SeqIO

def low_qual(L, q):
    i, j = 0, len(L)-1
    while L[i] < q:
        i+=1
    while L[j] < q:
        j-=1
    return i, j

with open('data/rosalind_bfil.txt', 'r') as f:
    q = int(f.readline().strip())

    with open('output.txt', 'w') as h:
        for record in SeqIO.parse(f, 'fastq'):
            i, j = low_qual(record.letter_annotations['phred_quality'], q)
            h.write('%s\n' % record[i:j+1].format('fastq'))
