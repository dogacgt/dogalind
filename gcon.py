#!/usr/bin/env python
#Global Alignment with Constant Gap Penalty

from Bio import SeqIO
import numpy as np

s, t = [str(record.seq) for record in SeqIO.parse('data/rosalind_gcon.txt', 'fasta')]

pro = 'A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y'.split()
scoring_matrix = np.loadtxt('data/blosum62.txt', dtype='i')
g = -5 #gap penalty

def _get_score(a, b):
    a_i, b_j = pro.index(a), pro.index(b)
    return scoring_matrix[a_i][b_j]

n, m = len(s), len(t)
S = np.zeros([m+1, n+1])
G1 = np.full([m+1, n+1], g)
G2 = np.full([m+1, n+1], g)

for i in range(1, m+1):
    S[i][0] = g
for i in range(1, n+1):
    S[0][i] = g

for i in range(1, m+1):
    for j in range(1, n+1):
        G1[i][j] = max(G1[i-1][j], S[i-1][j]+g)
        G2[i][j] = max(G2[i][j-1], S[i][j-1]+g)
        S[i][j] = max(S[i-1][j-1] + _get_score(s[j-1], t[i-1]), G1[i][j], G2[i][j])

print(int(S[-1][-1]))
