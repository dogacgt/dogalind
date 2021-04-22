#!/usr/bin/env python
#Base Quality Distribution

from Bio import SeqIO

with open('data/rosalind_bphr.txt', 'r') as f:
    q = int(f.readline())
    h = f.readlines()

    with open('fastq.txt', 'w') as l:
        for line in h:
            l.write(line)

    count = 0
    R = []
    for record in SeqIO.parse('fastq.txt', 'fastq'):
        quals = record.letter_annotations["phred_quality"]
        R.append(quals)
    for i in range(len(R[0])):
        if sum([r[i] for r in R])/len(R) < q:
            count += 1
    print(count)
