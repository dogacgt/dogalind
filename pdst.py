#!/usr/bin/env python
#Creating a Distance Matrix

import numpy as np
from Bio import SeqIO

L = []
for dna in SeqIO.parse('data/rosalind_pdst.txt', 'fasta'):
    L.append(dna.seq)

a = len(L)
A = np.zeros([a, a])

for i in range(a):
    for j in range(i, a):
        if i != j:
            count = 0
            for k in range(len(L[i])):
                if L[i][k] == L[j][k]:
                    count += 1
            pdist = 1-(count/len(L[i]))
            A[i][j] = pdist
            A[j][i] = pdist

with open('output.txt', 'w') as f:
    A = np.around(A, 5)
    for row in A:
        nums = ''
        for num in row:
            nums += str('%.5f' % num) + ' '
        f.write(nums + '\n')
