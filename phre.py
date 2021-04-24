#!/usr/bin/env python
#Read Quality Distribution

from Bio import SeqIO

with open('data/rosalind_phre.txt', 'r') as f:
    f = f.readlines()
    threshold = int(f[0].strip())
    with open('sample.txt', 'w') as h:
        for i in range(1, len(f)):
            h.write(f[i])

count = 0
for record in SeqIO.parse('sample.txt', 'fastq'):
    n = record.letter_annotations["phred_quality"]
    if sum(n)/len(n) < threshold:
        count += 1

print(count)
